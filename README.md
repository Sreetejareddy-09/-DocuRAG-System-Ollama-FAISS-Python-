# 📄 DocuRAG – Local Retrieval Augmented Generation System

DocuRAG is a **local RAG (Retrieval-Augmented Generation) system** built using **Ollama, FAISS, and Python**.  
It allows users to upload PDF documents, generate embeddings, store them in a vector database, and query them using a locally running LLM.

This project focuses on **privacy-first, offline document intelligence** without relying on cloud-based LLM APIs.

---

## 🚀 Features

- 📚 PDF document ingestion and text extraction  
- ✂️ Chunked text processing with overlap  
- 🧠 Semantic embeddings using Sentence Transformers  
- ⚡ Fast similarity search with FAISS  
- 🤖 Local LLM inference using Ollama  
- 🛠️ LLM execution managed via Python subprocess  
- 📊 Performance testing for latency and accuracy  

---

## 🏗️ Architecture Overview
PDFs → Text Extraction → Chunking → Embeddings → FAISS Vector Store
↓
Query Embedding
↓
Top-K Similar Chunks
↓
Ollama Local LLM
↓
Final Answer


---

## 🧰 Tech Stack

- **Python**
- **Ollama** (local LLM inference)
- **FAISS** (vector similarity search)
- **Sentence-Transformers** (`all-MiniLM-L6-v2`)
- **PyPDF**
- **Subprocess orchestration**

---

## 📂 Project Structure
├── ingest.py # PDF ingestion and FAISS index creation
├── query.py # Semantic search over vector store
├── query_with_ai.py # RAG pipeline with Ollama LLM
├── test_metrics.py # Latency testing for LLM inference
├── test_ollama.py # Basic Ollama connectivity test
├── test_ollama_query.py # Sample Ollama query test
├── requirements.txt
├── vectorstore/
│ ├── index.faiss
│ └── metadata.pkl
└── data/ # PDF documents


---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt


