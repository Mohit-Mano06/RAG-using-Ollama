import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")


print("---------------------- Working Environment ----------------------")

llm = ChatOllama(model_name = "llama3:8b", temperature=0.4)
## ------------ GROQ ------------
#llm = ChatGroq(groq_api_key = groq_api_key, model_name = "llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on provided context only.
    Please provide the most accurate response based on the question asked
    Context: {context}


    Question:{input}

    Answer in a clear and detailed way.
    If answer is not present in the context, then respond that the answer is not present in the context
    """

)


def create_vector_embeddings():
    embeddings = OllamaEmbeddings(model="qwen3-embedding:4b")
    docs = PyPDFLoader("").load()
    print("--------------------- DOCS LOADED ----------------------")
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 200)
    chunks = splitter.split_documents(docs)
    print("--------------------- CHUNKS CREATED ----------------------")

    vector = FAISS.from_documents(chunks, embeddings)
    print("--------------------- VECTOR STORED ----------------------")

    retriever = vector.as_retriever()
    rag_chain = (
        {
            "context":retriever,
            "input": RunnablePassthrough()
        }
        | prompt | llm
    )
    response = rag_chain.invoke(user_prompt)
    print(response.content)
    docs = retriever.invoke(user_prompt)
    print(docs)
  
if __name__ == "__main__":
    create_vector_embeddings()
    print("Vector Database is created")

