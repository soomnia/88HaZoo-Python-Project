# pip install SpeechRecognition
import speech_recognition as sr

# 오디오 파일 읽기
def from_file():
    # 음성 인식기 생성
    recognizer = sr.Recognizer()

    audio_file = "test.wav"

    # 오디오 파일 열기
    with sr.AudioFile(audio_file) as source:
        # 오디오 데이터 읽기
        audio_data = recognizer.record(source)

    try:
        # Google Web Speech API를 통해 음성 인식
        text = recognizer.recognize_google(audio_data, language='ko-KR')
        print("입력된 내용:", text)
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"Google Web Speech API 요청에 실패했습니다.\n{str(e)}")

    # OSError: FLAC conversion utility not available - consider installing the FLAC command line application by running `apt-get install flac` or your operating system's equivalent
    # 디바이스에 FLAC 설치하여 해결
    ## 맥OS
    ## brew install flac

# 마이크에서 음성을 받기
def from_microphone():

    ## pip install pyaudio
    # AttributeError: Could not find PyAudio; check installation
    # Failed to build pyaudio
    # ERROR: Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects
    # 디바이스에 portaudio 설치하여 해결
    ## 맥OS
    ## brew install portaudio

    # 음성 인식기 생성
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("음성을 기다리는 중!")
        audio = recognizer.listen(source)

    try:
        # Google Web Speech API를 통해 음성 인식
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("입력된 내용:", text)
        # 입력된 내용을 텍스트 파일로 저장
        with open("recorded.txt", "w") as file:
            file.write(text)
            print("텍스트가 저장되었습니다.")
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"Google Web Speech API 요청에 실패했습니다.\n{str(e)}")

# from_microphone()