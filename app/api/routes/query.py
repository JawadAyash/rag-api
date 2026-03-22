from fastapi import APIRouter
from app.schemas.query import QueryInput
from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.answer_service import generate_answer

router = APIRouter(prefix="/ask", tags=["query"])


@router.post("")
def ask_question(data: QueryInput):
    retrieved_chunks = retrieve_relevant_chunks(data.question)
    answer = generate_answer(data.question, retrieved_chunks)

    sources = [
        {
            "title": item.payload.get("title"),
            "content": item.payload.get("content"),
            "chunk_index": item.payload.get("chunk_index"),
        }
        for item in retrieved_chunks
    ]

    return {
        "question": data.question,
        "answer": answer,
        "retrieved_chunks_count": len(retrieved_chunks),
        "sources": sources,
    }