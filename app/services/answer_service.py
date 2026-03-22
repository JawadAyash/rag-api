from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def generate_answer(question: str, retrieved_chunks):
    context_block = "\n\n".join(
        [
            f"Title: {item.payload.get('title')}\nContent: {item.payload.get('content')}"
            for item in retrieved_chunks
        ]
    )

    prompt = f"""
You are a helpful AI knowledge assistant.

Answer the user's question using only the provided context.
If the context is not sufficient, say that the available documents do not contain enough information.

Context:
{context_block}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content.strip()