# RAG API — Retrieval-Augmented Generation Backend

A standalone Retrieval-Augmented Generation (RAG) API built with **FastAPI, OpenAI, and Qdrant**.

This project demonstrates a production-style backend for AI applications that require:

- document ingestion
- vector embeddings
- semantic search
- grounded LLM answers
- source-aware responses

The API allows adding documents, storing embeddings in a vector database, and answering questions using retrieved context.

---

## 🚀 Features

- FastAPI backend
- OpenAI embeddings
- Qdrant vector database
- Document ingestion endpoint
- Chunking pipeline
- Semantic retrieval
- Grounded answer generation
- Multi-document search
- Source tracking in responses
- Local Qdrant storage
- Environment config with `.env`

---

## 🧠 Architecture


Document → Chunk → Embedding → Qdrant
Question → Embedding → Vector Search → Context → LLM → Answer

app/
├── api/
│ └── routes/
│ ├── health.py
│ ├── documents.py
│ └── query.py
│
├── core/
│ └── config.py
│
├── schemas/
│ ├── document.py
│ └── query.py
│
├── services/
│ ├── chunker.py
│ ├── embedding_service.py
│ ├── vector_store.py
│ ├── retrieval_service.py
│ ├── answer_service.py
│ └── qdrant_client_service.py
│
└── main.py


---

## ⚙️ Tech Stack

- FastAPI
- Python
- OpenAI API
- Qdrant
- Uvicorn
- Pydantic
- python-dotenv

---

## 🔧 Installation

Clone the repo:


git clone https://github.com/JawadAyash/rag-api.git

cd rag-api

Create virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## 🔐 Environment Variables

Create `.env`


OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=rag_chunks


Local Qdrant storage will be used automatically.

---

## ▶ Run server

uvicorn app.main:app --reload

Open docs:

http://127.0.0.1:8000/docs

---

## 📥 Ingest document

POST `/documents/text`


{
"title": "Refund Policy",
"content": "Customers can request a refund within 14 days of purchase."
}

---

## ❓ Ask question

POST `/ask`

{
"question": "What is the refund policy?"
}

Response:


{
"answer": "...",
"retrieved_chunks_count": 1,
"sources": [...]
}


---

## 📦 Example Use Cases

- AI chatbot backend
- Knowledge base search
- Customer support AI
- Internal documentation search
- RAG experiments
- LLM grounding
- Vector DB learning project

---

## 📌 Future Improvements

- PDF ingestion
- File upload endpoint
- Metadata filtering
- Reranking
- Streaming responses
- Authentication
- Docker support
- Remote Qdrant
- LangChain integration

---

## 👨‍💻 Author

Jawad Ayash  
AI / Backend Developer  
GitHub: https://github.com/JawadAyash
