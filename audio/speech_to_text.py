# pip install python-multipart
import speech_recognition as sr
from io import BytesIO

# FIXME: pcm wav여야 사용 가능함
async def recognize_audio_file(file):
    recognizer = sr.Recognizer()

    audio_data = await file.read()
    audio_buffer = BytesIO(audio_data)

    print("*"*25)
    print("file:\n", file)
    print("file.filename:", file.filename)
    print("*"*25)

    try:
        with sr.AudioFile(audio_buffer) as source:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="ko-KR")
            print("사용자의 요청: ", text)
            first_word = extract_first_word(text)
            return first_word
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
        return None
    except sr.RequestError as e:
        print(f"API에 요청할 수 없습니다: {e}")
        return None
    

def extract_first_word(text):
    if text:
        return text.split()[0]
    else:
        return None
