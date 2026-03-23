from fastapi import APIRouter, UploadFile, File
from app.services.chunker import split_into_chunks
from app.services.embedding_service import generate_embedding
from app.services.vector_store import upsert_chunks
from app.services.pdf_reader import read_pdf


router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/file")
async def upload_file(file: UploadFile = File(...)):

    content_bytes = await file.read()

    if file.filename.lower().endswith(".txt"):

        content = content_bytes.decode("utf-8")

    elif file.filename.lower().endswith(".pdf"):

        content = read_pdf(content_bytes)

    else:
        return {"error": "Only .txt and .pdf supported"}

    chunks = split_into_chunks(content)

    payloads = []

    for i, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        payloads.append(
            {
                "title": file.filename,
                "content": chunk,
                "chunk_index": i,
                "embedding": embedding,
            }
        )

    upsert_chunks(payloads)

    return {
        "filename": file.filename,
        "chunks_created": len(payloads),
    }