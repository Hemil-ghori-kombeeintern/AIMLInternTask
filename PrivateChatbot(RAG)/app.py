import os
import shutil
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "data" / "uploads"
FAISS_DIR = BASE_DIR / "data" / "faiss"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
FAISS_DIR.mkdir(parents=True, exist_ok=True)


st.set_page_config(
    page_title="RAG PDF Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG PDF Assistant")

if not API_KEY:
    st.error(
        "GEMINI_API_KEY is missing. "
        "Please add it to your .env file."
    )
    st.stop()

@st.cache_resource
def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def split_text(text,chunk_size=600,chunk_overlap=120):

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):

        end = min(start + chunk_size,len(words))

        chunk = " ".join(
            words[start:end]
        )

        if chunk.strip():
            chunks.append(chunk)

        if end == len(words):
            break

        start = end - chunk_overlap

    return chunks


def create_vector_store(chunks):

    documents = [
        Document(
            page_content=chunk
        )
        for chunk in chunks
    ]

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    return vector_store

def save_vector_store(vector_store, pdf_name):

    folder_name = Path(pdf_name).stem

    store_path = FAISS_DIR / folder_name

    store_path.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(
        str(store_path)
    )

    return store_path


def load_vector_store(pdf_name):

    folder_name = Path(pdf_name).stem

    store_path = FAISS_DIR / folder_name

    index_file = store_path / "index.faiss"
    metadata_file = store_path / "index.pkl"

    if not index_file.exists():
        return None

    if not metadata_file.exists():
        return None

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        str(store_path),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def save_pdf(uploaded_file):

    pdf_path = UPLOAD_DIR / uploaded_file.name

    with open(pdf_path, "wb") as file:

        file.write(
            uploaded_file.getbuffer()
        )

    return pdf_path


@st.cache_resource
def get_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        google_api_key=API_KEY,
        temperature=0
    )


def create_rag_chain(vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 4
        }
    )

    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using ONLY the
        information in the context.

        If the answer is not available in
        the context, say:

        "I could not find the answer in the document."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    def format_documents(documents):

        return "\n\n".join(
            document.page_content
            for document in documents
        )

    rag_chain = (
        {
            "context": retriever | format_documents,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return rag_chain


uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


question = st.text_input(
    "Ask a question about the PDF"
)


if uploaded_file:

    pdf_name = uploaded_file.name

    pdf_path = UPLOAD_DIR / pdf_name

    if not pdf_path.exists():

        with st.spinner("Saving PDF..."):

            save_pdf(uploaded_file)


    else:

        st.info(
            f"PDF already exists: {pdf_path}"
        )


    vector_store = load_vector_store(
        pdf_name
    )

    if vector_store is None:

        with st.spinner(
            "Creating FAISS vector store..."
        ):

            text = extract_text_from_pdf(
                pdf_path
            )

            if not text.strip():

                st.error(
                    "No readable text found in the PDF."
                )

                st.stop()

            chunks = split_text(text)

            vector_store = create_vector_store(
                chunks
            )

            store_path = save_vector_store(
                vector_store,
                pdf_name
            )

        st.info(
            f"Created {len(chunks)} chunks."
        )

    else:

        st.success(
            "Existing FAISS vector store loaded."
        )



    if question:

        with st.spinner(
            "Searching PDF and generating answer..."
        ):

            rag_chain = create_rag_chain(
                vector_store
            )

            response = rag_chain.invoke(
                question
            )

        st.subheader("Answer")

        st.write(
            response.text
        )