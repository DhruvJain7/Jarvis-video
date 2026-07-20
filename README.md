# Jarvis-video
An AI meeting platform that transcribes video utilizing local Whisper (English).
It can even process Hindi/Hinglish using Sarvam AI.
It extracts insights from the Youtube video / meeting and generate bulleted summaries,key decisions and assigned action items if present.
In order to provide convenience to user it has RAG-powered chat interface using ChromaDB.

## What does this tool exactly do :
- Takes any Youtube url or audio / video file as input.
- Transcribes English meetings using local Whisper AI.
- Transcribes Hindi & Hinglish meetings using Sarvam AI.
- Summarizes the full meeting in bullet points.
- Extracts action items with owner and deadline.
- Extracts key decisions made in the meeting.
- Extracts open questions and follow-ups
- Lets you CHAT with your meeting using RAG + ChromaDB
- Export full report as PDF or TXT.
