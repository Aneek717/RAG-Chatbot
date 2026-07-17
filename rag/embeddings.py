from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(MODEL_NAME)

print(f"Loaded embedding model: {MODEL_NAME}")