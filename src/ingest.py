import os
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


def ingest(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print("PDF Loaded")

    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 200)
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")

    embeddings = OllamaEmbeddings(model = "nomic-embed-text:v1.5")

    vector_store = FAISS.from_documents(chunks, embeddings)
    print("FAISS Index Created")

    vector_store.save_local("vector_db")
    print("Vector Store Saved Locally")

    os.makedirs("data/vector_store", exist_ok=True)
    vector_store.save_local("data/vector_store")
    print("FIASS index saved at data/vector_store")

if __name__ == "__main__":
    ingest("-----------file_path_here----------")