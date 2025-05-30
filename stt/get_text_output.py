import os
import json
from groq import Groq
from python_dotenv import load_dotenv

load_dotenv()

client = Groq()

def text_output(file_path: str) -> str:
    """
    Transcribes the input audio file by the user into text.    
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path , 'rb') as file:
        transcription = client.audio.transcription.create(
            file = file,
            model = "distil-whisper-large-v3-en",
            language = "en",
        )
        
    return transcription.text