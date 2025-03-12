import streamlit as st

from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일의 환경 변수를 메모리에 로딩
load_dotenv(override= True)

# os.environ.get(".env의 변수가 들어가야함")
openai_key = os.environ.get("OPENAI_API_KEY")
# print(openai_key)

#OpenAI() 객체 생성
client = OpenAI(api_key=openai_key)

이미지 생성 함수 (user_prompt를 매개변수로 받음)
def get_image(user_prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=user_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        st.error(f"🚨 API 호출 중 오류 발생: {str(e)}")
        return None  # 오류 발생 시 None 반환



# UI 구현
st.title("🎨 그림 그리는 AI 화가 서비스")

# - 이미지 표시
st.image("images/robot_painter.jpg", width=200, caption="🤖 로봇 화가")

# - 설명 텍스트 출력
st.write("Tell me the picture you want. I'll draw it for you!")
st.write("원하는 이미지의 설명을 영어로 적어보세요")

# - textarea : 영어로 그림 설명 입력 (key 추가)
user_prompt = st.text_area("🎤 그림 설명을 입력하세요", height=200, key="unique_text_area")

# - 버튼 : GPT로부터 그림 요청
if st.button("🖌️ Painting"):
    if user_prompt.strip():
        image_url = get_image(user_prompt)  # user_prompt를 인자로 전달
        if image_url:
            st.image(image_url, width=300, caption="🎨 생성된 그림")
    else:
        st.warning("⚠️ 그림 설명을 입력하세요.")  # 입력이 없을 때 경고 메시지 출력
        
        
        