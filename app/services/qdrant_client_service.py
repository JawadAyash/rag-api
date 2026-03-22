from qdrant_client import QdrantClient
from app.core.config import settings

_qdrant_client = None


def get_qdrant_client():
    global _qdrant_client

    if _qdrant_client is not None:
        return _qdrant_client

    if settings.qdrant_url:
        _qdrant_client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            check_compatibility=False,
        )
    else:
        _qdrant_client = QdrantClient(path="qdrant_data")

    return _qdrant_client