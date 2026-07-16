import chromadb

from core.config import CHROMA_PATH

COLLECTION_NAME = "document_embeddings"

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)

print("Vector Store Loaded")