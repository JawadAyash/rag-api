from app.services.qdrant_client_service import get_qdrant_client
from app.services.embedding_service import generate_embedding
from app.core.config import settings


def retrieve_relevant_chunks(question: str, limit: int = 5):
    client = get_qdrant_client()
    query_vector = generate_embedding(question)

    results = client.query_points(
        collection_name=settings.qdrant_collection,
        query=query_vector,
        limit=limit,
    )

    return results.points