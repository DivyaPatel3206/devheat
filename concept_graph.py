from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

def extract_concepts(text):
    entities = ner(text[:1000])
    concepts = [entity['word'] for entity in entities]
    return concepts
