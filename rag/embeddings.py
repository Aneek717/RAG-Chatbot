from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5"

embedding_model = SentenceTransformer(MODEL_NAME)

print(f"Loaded embedding model: {MODEL_NAME}")