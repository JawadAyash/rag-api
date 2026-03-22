from pydantic import BaseModel


class TextDocumentInput(BaseModel):
    title: str
    content: str