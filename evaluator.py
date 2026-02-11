from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(student_answer, correct_answer):
    emb1 = model.encode(student_answer, convert_to_tensor=True)
    emb2 = model.encode(correct_answer, convert_to_tensor=True)
    score = util.pytorch_cos_sim(emb1, emb2)
    return float(score)
