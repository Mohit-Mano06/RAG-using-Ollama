# RAG System with Ollama & LangChain

A modular Retrieval-Augmented Generation (RAG) system built with Python, LangChain, and Ollama. This project allows you to ingest PDF documents, store them in a local vector database, and perform structured, context-aware queries using local LLMs.

## 🌟 Key Features

* **Advanced AI RAG Pipeline**: Combines local LLM inference (Llama 3) with vector-based retrieval for high-accuracy answers based purely on your documents.
* **Structured AI Responses**: Enforces the AI to return well-organized answers consisting of Definition, How it works, Why it is useful, and Examples.
* **Local Vector Database**: Uses FAISS for efficient, local vector storage, ensuring your data never leaves your machine.
* **Modular Architecture**: Clean separation of concerns between document ingestion (`ingest.py`), retrieval (`retriever.py`), and generation (`rag.py`).
* **Command-Line Interface**: Simple interactive CLI chat (`app.py`) to query your documents.

## 🛠️ Technology Stack

* **LangChain**: Orchestration framework for LLMs and tools.
* **Ollama**: Local execution of Large Language Models.
  * **Embeddings**: `nomic-embed-text:v1.5`
  * **Generation**: `llama3:8b`
* **FAISS**: Facebook AI Similarity Search for the local vector store.
* **PyPDF**: Document loading and processing.

## 📂 Project Structure

* `src/app.py`: The main entry point. Runs an interactive terminal chat loop to query the RAG system.
* `src/rich_app.py`: An alternative terminal chat loop built with `rich` for an enhanced UI. Safe to delete if migrating to a web frontend.
* `src/ingest.py`: Handles loading PDFs, chunking text, generating embeddings, and creating/saving the FAISS vector database.
* `src/rag.py`: Defines the prompt template and orchestrates the final generation using the LLM and the retrieved context.
* `src/retriever.py`: Responsible for loading the local FAISS vector store and configuring the retrieval mechanism.

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Ollama installed and running locally with the required models:
```bash
ollama pull llama3:8b
ollama pull nomic-embed-text:v1.5
```

### 2. Setup Dependencies
If you're using `uv` or `pip`, install the necessary Python packages:
```bash
uv pip install -r requirements.txt
```
OR
```bash
uv add -r requirements.txt
```

### 3. Ingest Documents
Place the path to your target PDF inside `src/ingest.py` and run it to create the vector database:
```bash
uv run src/ingest.py
```
This will create a `data/vector_store` directory containing the FAISS index.

### 4. Ask Questions
Start the interactive chat interface:
```bash
uv run src/app.py
```
Or for a premium terminal UI experience with spinners and panels, run:
```bash
uv run src/rich_app.py
```
Type your query and hit enter to see the structured AI response!