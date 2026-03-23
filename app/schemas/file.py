from pydantic import BaseModel


class FileUploadResponse(BaseModel):
    filename: str
    chunks_created: int