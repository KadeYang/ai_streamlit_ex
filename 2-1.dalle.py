
import streamlit as st
# openai key 값 로딩, 환경변수 .env에 저장, git에 업로딩은 안되도록
from openai import OpenAI
from dotenv import load_dotenv
import base64
import io
from PIL import Image
import os


# 환경변수 로딩
load_dotenv(override=True)

# 메모리에 로딩된 값을 api_key 변수에 대입
api_key = os.environ.get("OPENAI_API_KEY")
# openai key 값 프린트 해보기
# print(api_key)

# OpenAI 객체 생성
client = OpenAI(api_key=api_key)

# 실제이미지 값을 json값 리턴받음
def get_image(user_prompt):
    response = client.images.generate(
            model="dall-e-3",
            prompt=user_prompt,
            size = "1024x1024",
            quality="standard",            
            response_format='b64_json', # 이때 Base64 형태의 이미지를 리턴함
            n=1,
            
        )
    response = response.data[0].b64_json # DALLE로부터 Base64 형태의 이미지를 얻음.
    image_data = base64.b64decode(response) # Base64로 쓰여진 데이터를 이미지 형태로 변환
    image = Image.open(io.BytesIO(image_data)) # '파일처럼' 만들어진 이미지 데이터를 컴퓨터에서 볼 수 있도록 Open
    return image


# 1. 사용자에게 보여지는 부분 구현
# - 타이틀
st.title("그림 그리는 AI 화가 서비스 🌸")
# - 이미지표시
st.image("images/robot_painter.jpg", width=300, caption="로봇 화가")

# - 설명 텍스트 출력
st.write("원하는 그림을 말해주세요. 그려드리겠습니다.")
# st.write("원하는 이미지의 설명을 영어로 적어보세요.")
# - textarea : 영어로 그림그리기 설명 프롬프트 입력
user_prompt = st.text_area("원하는 이미지 설명을 영어로 적어보세요.", height=200)
# - 버튼 : 그림을 요청하기 gtp에게
# print("버튼클릭 전")
if st.button("Painting"):
    # 텍스트 에리어 박스에 입력한 값이 있는지 체크(user_prompt)
    print("user_prompt: ", user_prompt)
    if user_prompt:
        # print("프롬프트 값 정상")
        # openAI에 그림그리기 메시지 보내기, 함수 호출
        image = get_image(user_prompt)
        st.image(image, width=300, caption="로봇 화가 그림")
    else:
        # 그림기리기 요청을 입력하세요.
        st.write("텍스트 박스에 그림을 그릴 설명을 영어로 입력하세요.")
        pass