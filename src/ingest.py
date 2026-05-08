import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from config import get_embeddings, EMBEDDING_PROVIDER


def ingest(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print("PDF Loaded")

    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 200)
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")

    print(f"Using embedding provider: {EMBEDDING_PROVIDER}")
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(chunks, embeddings)
    print("FAISS Index Created")

    os.makedirs("data/vector_store", exist_ok=True)
    vector_store.save_local("data/vector_store")
    print("Vector store saved at data/vector_store")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = input("Enter path to PDF file: ").strip()
    ingest(pdf_path)