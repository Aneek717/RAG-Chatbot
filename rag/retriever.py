from rag.embeddings import embedding_model
from rag.vectorstore import collection


class RagRetriever:
    def __init__(self):
        self.embedding_model = embedding_model
        self.collection = collection

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.25
    ):
        # Generate embedding for the query
        query_embedding = self.embedding_model.encode(
            query,
            convert_to_numpy=True
        )

        # Query Chroma
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        retrieved_docs = []

        if results["documents"] and results["documents"][0]:

            documents = results["documents"][0]
            metadatas = results["metadatas"][0]
            distances = results["distances"][0]
            ids = results["ids"][0]

            for i, (doc, metadata, distance, doc_id) in enumerate(
                zip(documents, metadatas, distances, ids)
            ):
                similarity_score = 1 - distance

                if similarity_score >= score_threshold:
                    retrieved_docs.append(
                        {
                            "rank": i + 1,
                            "id": doc_id,
                            "document": doc,
                            "metadata": metadata,
                            "distance": distance,
                            "similarity_score": similarity_score,
                        }
                    )

        return retrieved_docs


rag_retriever = RagRetriever()