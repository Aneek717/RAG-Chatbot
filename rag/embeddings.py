from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
print("Before model load", flush=True)
embedding_model = SentenceTransformer(MODEL_NAME)
print("After model load", flush=True)

print(f"Loaded embedding model: {MODEL_NAME}")