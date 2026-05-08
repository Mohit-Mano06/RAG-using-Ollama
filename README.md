# 🤖 RAG System using OpenAI, Ollama, FAISS and LangChain

A modular and robust Retrieval-Augmented Generation (RAG) system built with **LangChain**, supporting both local **Ollama** models and cloud-based **OpenAI** APIs. This project allows you to ingest PDF documents, store them in a local vector database, and perform context-aware queries with a premium terminal interface.

---

## 🌟 Key Features

*   **🔄 Dual-Provider Support**: Seamlessly switch between **OpenAI (GPT-4o)** and **Ollama (Mistral/Llama 3)** for both embeddings and text generation via a simple `.env` toggle.
*   **✨ Premium Rich UI**: Includes an enhanced terminal interface (`rich_app.py`) with:
    *   Animated spinners during retrieval.
    *   Live-streaming responses in formatted panels.
    *   Color-coded logging and status updates.
*   **🧠 Structured AI Reasoning**: The system is engineered to provide well-organized answers consisting of:
    1.  **Definition**: A concise explanation.
    2.  **Mechanism**: How the concept works.
    3.  **Utility**: Why it is useful.
    4.  **Examples**: Practical scenarios (if found in context).
*   **⚡ Performance Metrics**: Real-time tracking of **latency** (generation time) and **source retrieval** (number of document pages handled).
*   **🔒 Local Vector Storage**: Uses **FAISS** for lightning-fast local vector searches, ensuring efficient retrieval without external database dependencies.

---

## 🛠️ Technology Stack

*   **Orchestration**: [LangChain](https://python.langchain.com/)
*   **LLM Providers**: OpenAI API & Ollama (Local)
*   **Vector Database**: FAISS (Facebook AI Similarity Search)
*   **PDF Processing**: PyPDF
*   **Terminal UI**: [Rich](https://github.com/Textualize/rich)
*   **Environment Management**: Dotenv & UV

---

## 📂 Project Structure

```text
├── data/
│   ├── vector_store/       # Local FAISS index (generated)
│   └── *.pdf               # Your source documents
├── src/
│   ├── config.py           # Centralized provider & model configuration
│   ├── ingest.py           # Document loading, chunking, and indexing
│   ├── retriever.py        # FAISS index loading and retrieval logic
│   ├── rag.py              # Prompt templates and LLM orchestration
│   ├── app.py              # Simple interactive CLI
│   └── rich_app.py         # Premium CLI with Rich UI & metrics
├── .env                    # API keys and provider selection
└── requirements.txt        # Project dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **Ollama** (Optional, for local mode): [Download here](https://ollama.com/)
  ```bash
  ollama pull mistral:7b
  ollama pull nomic-embed-text:v1.5
  ```

### 2. Configuration
Create a `.env` file from the example:
```bash
# Set your providers: "openai" or "ollama"
EMBEDDING_PROVIDER=openai
LLM_PROVIDER=openai

# If using OpenAI:
OPENAI_API_KEY=your_key_here
```

### 3. Setup Dependencies
We recommend using `uv` for fast package management:
```bash
uv pip install -r requirements.txt
```

### 4. Ingest Documents
Place your PDFs in the `data/` folder, then run:
```bash
uv run src/ingest.py
```

### 5. Start Questioning
Run the premium interactive UI:
```bash
uv run src/rich_app.py
```

---

## 📊 Performance Tracking
The system provides immediate feedback on every query:
- **Latency**: Measured in seconds from query to final character.
- **Handled Pages**: The exact number of relevant document chunks retrieved to form the answer.

---

## 📜 License
MIT License. Feel free to use and modify for your own RAG projects!
