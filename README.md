# RAG API — Retrieval Augmented Generation Backend

Standalone Retrieval-Augmented Generation (RAG) API built with FastAPI, OpenAI, and Qdrant.

This project demonstrates a production-style backend for AI applications that support:

- document ingestion
- TXT / PDF upload
- vector embeddings
- semantic search
- grounded LLM answers
- source-aware responses

The API allows uploading documents, storing embeddings in a vector database, and answering questions using retrieved context.

---

## 🚀 Features

- FastAPI backend
- OpenAI embeddings
- Qdrant vector database (local storage)
- Document ingestion via JSON
- TXT file ingestion
- PDF file ingestion
- Text chunking pipeline
- Semantic vector search
- Grounded answer generation
- Source tracking in responses
- Environment config with `.env`
- Clean project structure

---

## 🧠 Architecture


Document / File
↓
Chunking
↓
Embeddings (OpenAI)
↓
Vector Storage (Qdrant)
↓
User Question
↓
Embedding
↓
Vector Search
↓
Context
↓
LLM Answer


---

## 📁 Project Structure


app/
├── api/
│ └── routes/
│ ├── health.py
│ ├── documents.py
│ ├── query.py
│ └── file_upload.py
│
├── core/
│ └── config.py
│
├── schemas/
│ ├── document.py
│ ├── query.py
│ └── file.py
│
├── services/
│ ├── chunker.py
│ ├── embedding_service.py
│ ├── vector_store.py
│ ├── retrieval_service.py
│ ├── answer_service.py
│ ├── qdrant_client_service.py
│ └── pdf_reader.py
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
- pypdf

---

## 🔧 Installation

Clone the repo


git clone https://github.com/JawadAyash/rag-api.git

cd rag-api

Create virtual environment

python -m venv .venv
.venv\Scripts\activate

Install dependencies

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

Open docs

http://127.0.0.1:8000/docs

---

## 📥 Ingest text

POST `/documents/text`

{
"title": "Refund Policy",
"content": "Customers can request a refund within 14 days."
}

---

## 📂 Upload TXT / PDF

POST `/documents/file`

Supported:

- .txt
- .pdf

Upload using Swagger or multipart/form-data.

---

## ❓ Ask question

POST `/ask`

{
"question": "What is the refund policy?"
}

Response

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
- Chat with PDF
- Internal documentation search
- RAG experiments
- Vector DB learning project

---

## 📌 Future Improvements

- DOCX ingestion
- Metadata filtering
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