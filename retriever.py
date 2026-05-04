


from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

def load_retriever():
    embeddings = OllamaEmbeddings(model="nomic-embed-text:v1.5")
    vector_store = FAISS.load_local("data/vector_store", embeddings, allow_dangerous_deserialization=True)
    
    retriever = vector_store.as_retriever(
        search_kwargs = {"k" : 4}
    )

    return retriever
