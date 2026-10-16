"""Project-3: AIOps-Lite-HERO
Simple FastAPI app that implements a local RAG pipeline using ChromaDB and a private Ollama LLM endpoint.
Endpoints:
- GET / : health
- POST /ask : query ChromaDB and call Ollama for answer
- POST /ingest : ingest text into ChromaDB collection
"""
from fastapi import FastAPI
import chromadb, requests, os

app = FastAPI()
chroma = chromadb.Client()
collection = chroma.get_or_create_collection("devops-kb")

@app.get("/")
def root(): return {"status":"AIOps RAG Bot Running"}

@app.post("/ask")
def ask(q: str):
    # RAG: Search local ChromaDB
    docs = collection.query(query_texts=[q], n_results=2)
    context = str(docs)
    # LLM: Private Ollama - No OpenAI
    prompt = f"Context:{context}\nQuestion:{q}\nAnswer as DevOps expert:"
    res = requests.post("http://ollama:11434/api/generate", json={"model":"llama3.2:3b","prompt":prompt,"stream":False})
    return {"answer": res.json()['response'], "source": context}

@app.post("/ingest")
def ingest(text: str):
    collection.add(documents=[text], ids=[str(hash(text))])
    return {"ingested": True}
