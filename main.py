from fastapi import FastAPI, UploadFile, File
import shutil
from video_to_text import transcribe_video
from pdf_processor import extract_pdf_text
from summarizer import generate_notes
from concept_graph import extract_concepts
from quiz_generator import generate_quiz
from evaluator import evaluate_answer
from weak_topic import detect_weak_topics
from spaced_repetition import next_review
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# 1️⃣ Video to Notes
@app.post("/video-to-text/")
async def video_to_text(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe_video(path)
    return {"transcript": text}


# 2️⃣ PDF to Text
@app.post("/pdf-to-text/")
async def pdf_to_text(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_pdf_text(path)
    return {"text": text}


# 3️⃣ Generate Notes
@app.post("/generate-notes/")
async def notes(text: str):
    summary = generate_notes(text)
    return {"notes": summary}


# 4️⃣ Concept Graph
@app.post("/concepts/")
async def concepts(text: str):
    concept_list = extract_concepts(text)
    return {"concepts": concept_list}


# 5️⃣ Quiz Generator
@app.post("/generate-quiz/")
async def quiz(text: str):
    questions = generate_quiz(text)
    return {"quiz": questions}


# 6️⃣ Answer Evaluation
@app.post("/evaluate/")
async def evaluate(student_answer: str, correct_answer: str):
    score = evaluate_answer(student_answer, correct_answer)
    return {"similarity_score": score}


# 7️⃣ Weak Topic Detection
@app.post("/weak-topics/")
async def weak(results: dict):
    weak_topics = detect_weak_topics(results)
    return {"weak_topics": weak_topics}


# 8️⃣ Spaced Repetition
@app.post("/next-review/")
async def review(score: float):
    today = datetime.now()
    next_date = next_review(today, score)
    return {"next_review_date": next_date}
