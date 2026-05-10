
from fastapi import FastAPI
from pydantic import BaseModel
from src.rag import get_answer


print("This is the correct file!")

app = FastAPI()

class ChatRequest(BaseModel):
    message:str


@app.get("/")
def home():
    return {"messages": "Testinggg"}


@app.post("/chat")
def chat(request: ChatRequest):
    
    answer, docs_used = get_answer(request.message)

    return {
        "response": answer,
        "documents_used": docs_used
    }
