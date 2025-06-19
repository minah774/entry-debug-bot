import streamlit as st
import openai

# GPT 연결
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 웹앱 제목
st.title("🧠 엔트리 코드 오류 도우미")

# 입력창
entry_code = st.text_area("🔤 엔트리 블록 코드를 입력하세요", height=200)

# 버튼 누르면 실행
if st.button("분석하기"):
    if entry_code.strip() == "":
        st.warning("코드를 입력해주세요.")
    else:
        # 프롬프트 작성
        prompt = f"""
        다음은 초등학생이 짠 엔트리 블록 코드입니다.
        이 코드에 오류가 있다면:
        1. 어떤 블록이 문제인지
        2. 왜 문제가 되는지
        3. 어떻게 고치면 좋을지

        초등학생이 이해할 수 있게 설명해주세요.

        코드:
        {entry_code}
        """

        # GPT 요청
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            st.success("✅ 분석 결과:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
