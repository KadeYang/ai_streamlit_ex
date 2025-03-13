####### lib 설치 ##########
# pip install openai
# pip install streamlit
# pip install python-dotenv
###########################
# 실행 : streamlit run 2-3.voice.py
###########################
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일 경로 지정 
load_dotenv(override=True)

# Open AI API 키 설정하기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI Key 값 셋팅
client = OpenAI(api_key = api_key)


# 음성 변환 함수
def text_to_voice(user_prompt,selected_option):
    audio_response = client.audio.speech.create(
        model="tts-1",
        voice=selected_option,
        input=user_prompt,
    )
    
    audio_content = audio_response.content
    return audio_content

# audio 저장하기
def save_audio(audio_content):
    with open("temp_audio.mp3", "wb") as audio_file:
        #audio_content 저장된 값을 오디오 파일로 저장
        audio_file.write(audio_content)

# 메인 처리 로직
def main():


    #뷰포트에 h1테그로 텍스트 출력
    st.title("OpenAI's Text-to-Audio Response")

    # 달리가 생성한 이미지를 사용. prompt: 귀여운 인공지능 성우 로봇 그려줘
    st.image("https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%84%B1%EC%9A%B0.jpg", width=200)

    # 인공지능 성우 선택 박스를 생성.
    # 공식 문서 참고: https://platform.openai.com/docs/guides/text-to-speech
    options = ['alloy', 'ash', 'coral', 'echo', 'fable', 'onyx', 'nova', 'sage', 'shimmer']


    # 뷰포트에 선택목록을 표시하고, 사용자가 선택하면 select_option
    selected_option = st.selectbox("성우를 선택하세요:", options)

    # 문자열 default_text 변수에 대입
    default_text = '오늘은 생활의 꿀팁을 알아보겠습니다.'
    # 텍스트 박스 표시, 레이블 출력, 초기값 출력 
    # 사용자가 값을 입력하면 user_prompt에 대입
    user_prompt = st.text_area("인공지능 성우가 읽을 스크립트를 입력해주세요.", value=default_text, height=200)

    # Generate Audio 버튼을 클릭하면 True가 되면서 if문 실행.
    if st.button("Generate Audio"):

        # 텍스트로부터 음성을 생성.
        # selected_option, user_prompt 값으로 tts-1 모델에 음성생성 요청
        #text_to_voice 함수로 호출
        

        #리턴 값에서 오디오만 추출
        audio_content = text_to_voice(user_prompt,selected_option)

        # 음성을 mp3 파일로 저장.
        # 바이너리로 쓰겠다(음성 데이터), audio_file : 파일변수
        save_audio(audio_content)
        
        # audio 컨트롤러 표시, mp3 파일을 재생.
        st.audio("temp_audio.mp3", format="audio/mp3")
    
# 메인 실행
if __name__ == "__main__":
    main()