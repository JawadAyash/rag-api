from pypdf import PdfReader


def read_pdf(file_bytes: bytes) -> str:
    from io import BytesIO

    pdf = PdfReader(BytesIO(file_bytes))

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text