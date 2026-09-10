import os
import faiss

from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv

load_dotenv()


with open(
    "documents/company_info.txt",
    "r",
    encoding="utf-8"
) as file:

    text = file.read()


def create_chunks(
    text,
    chunk_size=300
):

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


chunks = create_chunks(text)



embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



embeddings = embedding_model.encode(
    chunks
)


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)



def retrieve(query,top_k=3):
    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(query_embedding,top_k)

    results = []

    for i in indices[0]:
        if i < len(chunks):
            results.append(
                chunks[i]
            )

    return results


api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:

client = genai.Client(
    api_key=api_key
)


def ask_rag(question):

    retrieved_chunks = retrieve(
        question
    )

    context = "\n\n".join(
        retrieved_chunks
    )


    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY
the provided context.

If the answer is not present
in the context, say:

"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


question = input(
    "Ask a question: "
)

answer = ask_rag(
    question
)

print("\nAnswer:")
print(answer)