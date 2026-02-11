from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def generate_notes(text):
    prompt = f"Create structured study notes from this:\n{text}"
    result = generator(prompt, max_length=300)
    return result[0]["generated_text"]
