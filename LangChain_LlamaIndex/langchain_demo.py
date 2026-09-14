import os

from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file"
    )


# ============================================================
# 2. DOCUMENT LOADING
# ============================================================

loader = TextLoader(
    "company_info.txt",
    encoding="utf-8"
)

documents = loader.load()

print("Number of documents:", len(documents))
for index, document in enumerate(documents, start=1):
    print(f"\nDocument {index}:")
    print(document.page_content)


# ============================================================
# 3. TEXT SPLITTING / CHUNKING
# ============================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

chunks = text_splitter.split_documents(
    documents
)

print("Number of chunks:", len(chunks))
for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}:")
    print(chunk.page_content)


# ============================================================
# 4. CREATE EMBEDDINGS
# ============================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("\nEmbedding model created:", embedding_model.model_name)


# ============================================================
# 5. CREATE FAISS VECTOR DATABASE
# ============================================================

vectorstore = FAISS.from_documents(
    chunks,
    embedding_model
)

print("FAISS vector database created with", len(chunks), "chunks")


# ============================================================
# 6. CREATE RETRIEVER
# ============================================================

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 3
    }
)

print("Retriever created with k=3")


# ============================================================
# 7. CREATE PROMPT
# ============================================================

prompt = ChatPromptTemplate.from_template(
    """
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
)


# ============================================================
# 8. CREATE GEMINI LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=api_key
)


# ============================================================
# 9. CREATE RAG FUNCTION
# ============================================================

def ask_rag(question):

    # Retrieve relevant documents
    retrieved_documents = retriever.invoke(
        question
    )

    print("\nRetrieved documents:")
    for index, document in enumerate(retrieved_documents, start=1):
        print(f"\nRetrieved document {index}:")
        print(document.page_content)

    # Convert documents into text
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    print("\nGenerated context:")
    print(context)

    # Create prompt
    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    print("\nGenerated prompt:")
    print(final_prompt.to_string())

    # Ask Gemini
    response = llm.invoke(
        final_prompt
    )

    print("\nGenerated model response:")
    print(response.content)

    return response.content


# ============================================================
# 10. ASK QUESTION
# ============================================================

question = input(
    "Ask a question: "
)

answer = ask_rag(
    question
)

print("\nAnswer:")
if isinstance(answer, list):
    for block in answer:
        if isinstance(block, dict):
            print(block.get("text", ""))
        else:
            print(block)
else:
    print(answer)