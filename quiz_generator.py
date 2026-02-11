from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_quiz(text):
    prompt = f"Generate 3 MCQ questions from this text:\n{text[:1000]}"
    result = generator(prompt, max_length=300)
    return result[0]["generated_text"]
