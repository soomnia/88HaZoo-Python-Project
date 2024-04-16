from fastapi.responses import StreamingResponse

# pip install gTTS
from gtts import gTTS

# pip install moviepy
# brew install ffmpeg
from moviepy.editor import AudioFileClip

import io

async def text_to_speech(text: str):
    try:
        print("text_to_speech:", text)

        tts = gTTS(text, lang='ko')

        audio_data = io.BytesIO()

        tts.write_to_fp(audio_data)
        
        audio_data.seek(0)

        ## 서버에 파일 저장
        # tts.save(filename)
        # time.sleep(0.5)
        ## 서버에 있는 파일을 변환
        # wav_to_pcm_wav(filename)

        return StreamingResponse(io.BytesIO(audio_data.read()), media_type="audio/wav")
    except :
        return {"error": f"'{text}'를 음성 파일로 만드는 것에 실패했습니다."}

def wav_to_pcm_wav(filename: str):
    clip = AudioFileClip(filename)
    clip.write_audiofile("tts_test_pcm.wav", codec="pcm_s16le", ffmpeg_params=["-ar", "16000"])
