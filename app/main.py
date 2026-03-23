from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import settings
from app.api.routes.documents import router as documents_router
from app.api.routes.query import router as query_router
from app.api.routes.file_upload import router as file_router

print("Collection:", settings.qdrant_collection)
app = FastAPI(title="RAG API")

@app.get("/")
def root():
    return {"message": "RAG API is running"}


app.include_router(health_router)
app.include_router(documents_router)
app.include_router(query_router)
app.include_router(file_router)