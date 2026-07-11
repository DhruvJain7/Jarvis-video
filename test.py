from core.transcriber import transcribe_all
from utils.audio_processor import process_input

source = "https://www.youtube.com/watch?v=ZVPlLaehjLk"

chunks = process_input(source)

print(transcribe_all(chunks))
