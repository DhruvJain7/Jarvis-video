from dotenv import load_dotenv
load_dotenv()
from core.transcriber import transcribe_all
from utils.audio_processor import process_input
import os

print("KEY LOADED:" , os.getenv("SARVAM_API_KEY"))
print("CWD", os.getcwd())
source = "https://www.youtube.com/watch?v=OqyejuqLh14"
language = "hinglish"

chunks = process_input(source)
transcript = transcribe_all(chunks,language=language)

print("\n === Transcript ===\n")
print(transcript)
