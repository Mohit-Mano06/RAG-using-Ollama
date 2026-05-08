"""
config.py — Central provider configuration.

Set EMBEDDING_PROVIDER and LLM_PROVIDER in your .env file:
  EMBEDDING_PROVIDER=openai   # or "ollama"
  LLM_PROVIDER=openai         # or "ollama"

Switching is as simple as changing those two lines and re-ingesting
if you change the embedding provider (vectors must match the model used).
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── Provider selection ────────────────────────────────────────────────────────
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "openai").lower()
LLM_PROVIDER       = os.getenv("LLM_PROVIDER", "openai").lower()

# ── Model names (override in .env if you want a different model) ──────────────
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
OPENAI_LLM_MODEL       = os.getenv("OPENAI_LLM_MODEL", "gpt-5.4-nano")

OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text:v1.5")
OLLAMA_LLM_MODEL       = os.getenv("OLLAMA_LLM_MODEL", "mistral:7b")


def get_embeddings():
    """Return the embedding object for the configured provider."""
    if EMBEDDING_PROVIDER == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)
    elif EMBEDDING_PROVIDER == "ollama":
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(model=OLLAMA_EMBEDDING_MODEL)
    else:
        raise ValueError(
            f"Unknown EMBEDDING_PROVIDER='{EMBEDDING_PROVIDER}'. "
            "Valid values: 'openai', 'ollama'"
        )


def get_llm(temperature: float = 0.4):
    """Return the LLM object for the configured provider."""
    if LLM_PROVIDER == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=OPENAI_LLM_MODEL, temperature=temperature)
    elif LLM_PROVIDER == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=OLLAMA_LLM_MODEL, temperature=temperature)
    else:
        raise ValueError(
            f"Unknown LLM_PROVIDER='{LLM_PROVIDER}'. "
            "Valid values: 'openai', 'ollama'"
        )
