
from langchain_community.vectorstores import FAISS
from .config import get_embeddings, EMBEDDING_PROVIDER


def load_retriever():
    embeddings = get_embeddings()
    print(f"[retriever] Using embedding provider: {EMBEDDING_PROVIDER}")
    vector_store = FAISS.load_local("data/vector_store", embeddings, allow_dangerous_deserialization=True)
    
    retriever = vector_store.as_retriever(
        search_kwargs = {"k" : 4}
    )

    return retriever
