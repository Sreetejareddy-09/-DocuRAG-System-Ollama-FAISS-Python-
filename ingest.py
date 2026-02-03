import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

print("🔄 Loading PDFs...")

documents = []

# Load PDFs from the data folder
for file in os.listdir("C:\\Users\\sreet\\documind-rag\\venv\\data"):
    if file.endswith(".pdf"):
        pdf_path = os.path.join("C:\\Users\\sreet\\documind-rag\\venv\\data", file)
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        documents.append({"text": text, "source": file})

print(f"📄 Loaded {len(documents)} documents")

# Simple text splitter
def split_text(documents, chunk_size=500, chunk_overlap=50):
    chunks = []
    for doc in documents:
        text = doc["text"]
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            chunks.append({"text": chunk_text, "source": doc["source"]})
            start += chunk_size - chunk_overlap
    return chunks

chunks = split_text(documents)
print(f"✂️ Created {len(chunks)} text chunks")

# Load sentence-transformers model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create embeddings
embeddings = [model.encode(chunk["text"]) for chunk in chunks]

# Create FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype="float32"))

# Save FAISS index and metadata
os.makedirs("vectorstore", exist_ok=True)
faiss.write_index(index, "vectorstore/index.faiss")
with open("vectorstore/metadata.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ Vector database created successfully!")



