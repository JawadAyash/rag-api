# RAG API

Standalone Retrieval-Augmented Generation (RAG) API built with FastAPI, OpenAI, and Qdrant.

## Features

- FastAPI backend
- Document ingestion via API
- Text chunking
- OpenAI embeddings
- Qdrant vector storage
- Semantic retrieval
- Grounded answer generation
- Returned retrieval sources for transparency

## Tech Stack

- FastAPI
- OpenAI API
- Qdrant
- Python
- Uvicorn
- python-dotenv

## Endpoints

### Health
- `GET /`
- `GET /health`
- `GET /qdrant-check`

### Documents
- `POST /documents/text`

### Query
- `POST /ask`

## Example Flow

1. Ingest a document with `POST /documents/text`
2. Ask a question with `POST /ask`
3. Receive:
   - grounded answer
   - retrieved chunk count
   - source chunks used

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt