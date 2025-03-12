import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# API 키 가져오기
openai_key = os.getenv("OPENAI_API_KEY")

# API 키가 없으면 경고 출력
if not openai_key:
    st.error("❌ OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
else:
    st.success("✅ API 키가 정상적으로 로드되었습니다.")

# OpenAI 클라이언트 생성
try:
    client = OpenAI(api_key=openai_key)
except Exception as e:
    st.error(f"🚨 OpenAI 클라이언트 생성 실패: {str(e)}")

# Streamlit UI
st.title("🎨 AI 그림 생성 서비스")

# 이미지 설명 입력 (key 추가)
user_prompt = st.text_area("그림 설명을 입력하세요:", height=200, key="unique_text_area")

# 버튼 클릭 시 API 호출
if st.button("🖌️ Painting"):
    if user_prompt.strip():
        try:
            # OpenAI API를 사용하여 DALL·E 이미지 생성
            response = client.images.generate(  # create → generate로 변경
                model="dall-e-3",
                prompt=user_prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )

            # 응답이 정상인지 확인
            if response and response.data:
                image_url = response.data[0].url
                st.image(image_url, caption="🖼️ Generated Image", use_column_width=True)
            else:
                st.error("⚠️ API 응답이 올바르지 않습니다. 다시 시도해 주세요.")

        except Exception as e:
            st.error(f"🚨 API 호출 중 오류 발생: {str(e)}")  # 정확한 에러 메시지 확인

    else:
        st.warning("⚠️ 그림 설명을 입력하세요.")  # 사용자 입력이 없을 때 경고 메시지 출력

