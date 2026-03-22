from fastapi import APIRouter
from app.services.qdrant_client_service import get_qdrant_client

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/qdrant-check")
def qdrant_check():
    client = get_qdrant_client()
    collections = client.get_collections()
    return {
        "status": "connected",
        "collections": [c.name for c in collections.collections],
    }