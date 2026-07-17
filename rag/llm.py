from langchain_groq import ChatGroq

from core.config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model_name=MODEL_NAME,
    temperature=0.6,
    api_key=GROQ_API_KEY
)