from rag.pipeline import rag_query


def chat(query: str):
    return rag_query(query)