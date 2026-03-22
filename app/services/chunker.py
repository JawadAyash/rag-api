def split_into_chunks(text: str, max_length: int = 300) -> list[str]:
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        candidate = f"{current_chunk}. {sentence}".strip(". ").strip() if current_chunk else sentence

        if len(candidate) <= max_length:
            current_chunk = candidate
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    return chunks