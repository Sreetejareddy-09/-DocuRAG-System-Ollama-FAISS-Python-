import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

# Load FAISS index and metadata
index = faiss.read_index("vectorstore/index.faiss")
with open("vectorstore/metadata.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Function to query the vector database
def query_vectorstore(question, top_k=3):
    # Encode question
    q_emb = model.encode(question).reshape(1, -1).astype("float32")
    
    # Search in FAISS
    distances, indices = index.search(q_emb, top_k)
    
    results = []
    for i in indices[0]:
        chunk = chunks[i]
        results.append(chunk["text"])
    return results

# Interactive loop
print("💬 Ask questions about your PDFs! Type 'exit' to quit.")
while True:
    question = input("\nYour question: ")
    if question.lower() in ["exit", "quit"]:
        break
    answers = query_vectorstore(question)
    print("\n🔹 Top answers:")
    for i, ans in enumerate(answers, 1):
        print(f"{i}. {ans}\n")
