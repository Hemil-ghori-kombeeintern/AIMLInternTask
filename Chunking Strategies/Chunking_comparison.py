import re
from transformers import AutoTokenizer
from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
Python is a popular programming language used for
web development, automation, data science, and
machine learning.

Machine learning is a branch of artificial intelligence.
It allows computers to learn patterns from data.

Deep learning is a subset of machine learning.
It uses neural networks with multiple layers.

Pandas is a Python library used for data manipulation
and analysis. NumPy provides numerical computing
capabilities and multidimensional arrays.
"""


# ------------------------------------------------
# 1. Fixed-size chunking
# ------------------------------------------------

def fixed_chunking(text, chunk_size=200):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


# ------------------------------------------------
# 2. Fixed-size + overlap
# ------------------------------------------------

def fixed_overlap_chunking(text,chunk_size=200,overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


# ------------------------------------------------
# 3. Sentence chunking
# ------------------------------------------------

def sentence_chunking(text,sentences_per_chunk=2):
    sentences = re.split(r'(?<=[.!?])\s+',text.strip())
    chunks = []
    for i in range(0,len(sentences),sentences_per_chunk):

        chunk = " ".join(sentences[i:i + sentences_per_chunk])

        chunks.append(chunk)

    return chunks


# ------------------------------------------------
# 4. Paragraph chunking
# ------------------------------------------------

def paragraph_chunking(text):

    paragraphs = text.split("\n\n")

    return [
        paragraph.strip()
        for paragraph in paragraphs
        if paragraph.strip()
    ]


# ------------------------------------------------
# 5. Token-based chunking
# ------------------------------------------------

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def token_chunking(text,chunk_size=100,overlap=20):

    tokens = tokenizer.encode(text,add_special_tokens=False)

    chunks = []
    start = 0
    while start < len(tokens):

        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk = tokenizer.decode(
            chunk_tokens,
            skip_special_tokens=True
        )

        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


# ------------------------------------------------
# 6. Recursive chunking
# ------------------------------------------------

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)


def recursive_chunking(text):

    return recursive_splitter.split_text(text)


# ------------------------------------------------
# Run all strategies
# ------------------------------------------------

strategies = {
    "Fixed Size": fixed_chunking(text),
    "Fixed + Overlap": fixed_overlap_chunking(text),
    "Sentence": sentence_chunking(text),
    "Paragraph": paragraph_chunking(text),
    "Token": token_chunking(text),
    "Recursive": recursive_chunking(text)
}


# ------------------------------------------------
# Display results
# ------------------------------------------------

for strategy, chunks in strategies.items():

    print("\n")
    print("=" * 70)
    print(strategy)
    print("=" * 70)

    print("Number of chunks:", len(chunks))

    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i + 1}:")
        print(chunk)