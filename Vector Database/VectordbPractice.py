from sentence_transformers import SentenceTransformer
import faiss



documents = [
    "Python is a popular programming language used for web development, automation, data science, and machine learning.",
    "Machine learning is a branch of artificial intelligence where computers learn patterns from data.",
    "PyTorch is an open-source deep learning framework used to build and train neural networks.",
    "Pandas is a Python library used for data manipulation and analysis.",
    "NumPy provides powerful numerical computing capabilities and multidimensional arrays.",
    "Computer vision is a field of artificial intelligence that enables computers to understand images and videos."
]


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


embeddings = embedding_model.encode(
    documents
)

print("Embedding shape:",embeddings.shape)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Vectors stored:",index.ntotal)

query = ("What is used to build neural networks?")

query_embedding = embedding_model.encode(
    [query]
)

k = 3 

distances, indices = index.search(
    query_embedding,
    k
)

print("\nSearch Results:\n")
print("distances:",distances)
print("indices:",indices)

for rank, index_id in enumerate(indices[0]):

    print(f"Result {rank + 1}")
    print(documents[index_id])
    print("Distance:",distances[0][rank])

    print("-" * 60)