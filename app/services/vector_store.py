from qdrant_client.models import PointStruct, VectorParams, Distance
from app.services.qdrant_client_service import get_qdrant_client
from app.core.config import settings


def ensure_collection(vector_size: int):
    client = get_qdrant_client()
    collections = client.get_collections().collections
    names = [collection.name for collection in collections]

    if settings.qdrant_collection not in names:
        client.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )


def upsert_chunks(chunks: list[dict]):
    if not chunks:
        return

    client = get_qdrant_client()
    vector_size = len(chunks[0]["embedding"])

    ensure_collection(vector_size)

    points = []

    for index, chunk in enumerate(chunks):
        points.append(
            PointStruct(
                id=index + 1,
                vector=chunk["embedding"],
                payload={
                    "title": chunk["title"],
                    "content": chunk["content"],
                    "chunk_index": chunk["chunk_index"],
                },
            )
        )

    client.upsert(
        collection_name=settings.qdrant_collection,
        points=points,
    )