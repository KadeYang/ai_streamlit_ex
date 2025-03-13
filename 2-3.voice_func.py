# ####### lib 설치 ##########
# # pip install openai
# # pip install streamlit
# # pip install python-dotenv
# ###########################
# # 실행 : streamlit run 2-3.voice.py
# ###########################
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


# 음성 변환 함수
def text_to_voice(client, text, voice="alloy"):
    try:
        audio_response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
        )
        return audio_response.content
    except Exception as e:
        st.error(f"음성 변환 오류 발생: {str(e)}")
        return None

# 오디오 저장 함수
def save_audio(audio_content, filename="temp_audio.mp3"):
    """변환된 음성을 mp3 파일로 저장"""
    try:
        with open(filename, "wb") as audio_file:
            audio_file.write(audio_content)
        return filename  # 저장된 파일 이름 반환
    except Exception as e:
        st.error(f"오디오 저장 오류 발생: {str(e)}")
        return None

#메인으로 묶기
def main():
    # .env 파일 경로 지정 
    load_dotenv(override=True)

    # Open AI API 키 설정하기
    api_key = os.getenv('OPENAI_API_KEY')

    # OpenAI Key 값 셋팅
    client = OpenAI(api_key = api_key)
    st.title("🎙️ AI 성우: 텍스트를 음성으로 변환해드립니다!")
    st.image("https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%84%B1%EC%9A%B0.jpg", width=200)
    
    voice_options = [
        
        'alloy',
        'ash',
        'coral',
        'echo',
        'fable',
        'onyx',
        'nova',
        'sage',
        'shimmer'
    ]
    selected_voice = st.selectbox("🎭 성우를 선택하세요:", voice_options)
    
    # 인공지능 성우에게 프롬프트 전달
    default_text = "오늘은 생활의 꿀팁을 알아보겠습니다."
    user_prompt = st.text_area("📜 AI 성우가 읽을 텍스트를 입력하세요.", value=default_text, height=200)
    
    # 음성 생성 버튼
    if st.button("🎤 음성 생성"):
        if user_prompt.strip():
            st.info("🎧 음성을 생성 중입니다...")

            audio_content = text_to_voice(client, user_prompt, selected_voice)
            if audio_content:
                audio_file = save_audio(audio_content)
                if audio_file:
                    st.success("✅ 음성이 생성되었습니다!")
                    st.audio(audio_file, format="audio/mp3")
        else:
            st.warning("⚠️ 텍스트를 입력해주세요.")

if __name__ == "__main__":
    main()
    


    




