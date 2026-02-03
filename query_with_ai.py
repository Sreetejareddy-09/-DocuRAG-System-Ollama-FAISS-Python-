import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import subprocess

# Load FAISS index
index = faiss.read_index("vectorstore/index.faiss")

# Load metadata (chunks)
with open("vectorstore/metadata.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Path to your Ollama executable
ollama_path = r"C:\Users\sreet\AppData\Local\Programs\Ollama\ollama.exe"

# Function to query Ollama
def ask_ollama(prompt_text):
    result = subprocess.run(
        [ollama_path, "run", "llama2", prompt_text],
        capture_output=True,
        text=True
    )
    return result.stdout

# Function to search top chunks
def search_chunks(query, top_k=3):
    query_embedding = model.encode(query)
    distances, indices = index.search(query_embedding.reshape(1, -1), top_k)
    top_chunks = [chunks[i]["text"] for i in indices[0]]
    return "\n".join(top_chunks)

# Chat loop
print("💬 Ask questions about your PDFs (type 'exit' to quit).")
while True:
    question = input("\nYour question: ")
    if question.lower() == "exit":
        break

    # Get top relevant chunks
    top_chunks_text = search_chunks(question)

    # Ask Ollama
    answer = ask_ollama(top_chunks_text)
    print("\n🔹 AI Answer:\n", answer)
