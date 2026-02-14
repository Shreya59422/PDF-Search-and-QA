# PDF-Search-and-QA

PDF-Search-and-QA is a document question-answering system built using Retrieval-Augmented Generation (RAG).

Project Overview

This project demonstrates:
- Document parsing
- Text chunking
- Embedding generation
- Vector similarity search
- Local language model integration

System Architecture

1. User uploads a PDF.
2. Text is cleaned and split into chunks.
3. Embeddings are generated.
4. Embeddings are stored in FAISS.
5. User query retrieves relevant chunks.
6. Retrieved context is passed to Phi model.
7. Model generates contextual answer.

Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Ollama
- Phi Model

Setup Instructions

Clone the repository:
git clone https://github.com/YOUR_USERNAME/PDF-Search-and-QA.git

Install dependencies:
pip install -r requirements.txt

Install Ollama:
https://ollama.com/download

Pull model:
ollama pull phi

Run application:
streamlit run app.py

Features

- Upload PDF
- Semantic retrieval
- Context-aware answers
- Chat interface
- Fully offline

Limitations

- Performance depends on CPU
- Smaller local models give shorter answers
- Prototype system

Purpose

This project demonstrates practical implementation of RAG architecture for document intelligence systems.
