from fastapi import APIRouter, File, UploadFile
from audio.speech_to_text import recognize_audio_file
from audio.text_to_speech import text_to_speech

router = APIRouter(prefix="/api/v1/weather", tags=["crawling"])

@router.post("/upload/audio")
async def upload_audio_file(file: UploadFile = File(...)):
    message = await recognize_audio_file(file)
    
    return message

@router.get("/download/audio")
async def text_to_audio(text: str):
    response = await text_to_speech(text)
    return response
