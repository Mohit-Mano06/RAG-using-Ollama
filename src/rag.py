from langchain_core.prompts import ChatPromptTemplate
from retriever import load_retriever
from config import get_llm, LLM_PROVIDER
import os

llm = get_llm(temperature=0.4)
print(f"[rag] Using LLM provider: {LLM_PROVIDER}")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based only on the context below/

    Structure your answer as: 
    1. Definition
    2. How it works
    3. Why it is useful
    4. Example (if mentioned in the context)

    Guidelines: 
    - Combine information from multiple parts of the context
    - Be confident and clear
    - Do NOT say "the context says" or "the context mentions"
    - If information is missing, say what is missing briefly and continue with available info
    Context:
    {context}

    Question:
    {question}

    If the answer is not in the context, say:
    "The answer is not present in the provided document"
    
    """
)


def get_answer(user_query: str):
    retriever = load_retriever()

    docs = retriever.invoke(user_query)

    context = "\n\n".join([doc.page_content for doc in docs])

    final_prompt = prompt.format(
        context = context,
        question = user_query
    )

    return llm.stream(final_prompt), len(docs)