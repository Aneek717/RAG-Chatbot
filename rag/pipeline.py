from langchain_core.messages import SystemMessage, HumanMessage

from rag.llm import llm
from rag.retriever import rag_retriever
from rag.prompt import SYSTEM_PROMPT


def rag_query(query: str, top_k=3):

    # 1. Retrieve documents
    retrieved_docs = rag_retriever.retrieve(
        query=query,
        top_k=top_k,
        score_threshold=0.3
    )

    # 2. No relevant documents found
    if not retrieved_docs:
        return "I can't provide that information."

    # 3. Build context
    context = "\n\n".join(
        [
            f"Document {doc['rank']}:\n{doc['document']}"
            for doc in retrieved_docs
        ]
    )

    # 4. Create user prompt
    user_prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_prompt)
    ]

    # 5. Generate answer
    response = llm.invoke(messages)

    return response.content