from fastapi import APIRouter
from app.schemas.document import TextDocumentInput
from app.services.chunker import split_into_chunks
from app.services.embedding_service import generate_embedding
from app.services.vector_store import upsert_chunks

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/text")
def add_text_document(data: TextDocumentInput):
    raw_chunks = split_into_chunks(data.content)

    chunk_payloads = []

    for index, chunk_text in enumerate(raw_chunks):
        embedding = generate_embedding(chunk_text)

        chunk_payloads.append(
            {
                "title": data.title,
                "content": chunk_text,
                "chunk_index": index,
                "embedding": embedding,
            }
        )

    upsert_chunks(chunk_payloads)

    return {
        "message": "Document ingested successfully",
        "title": data.title,
        "chunks_created": len(chunk_payloads),
    }