PDF-Search-and-QA

PDF-Search-and-QA is a document question-answering system built using Retrieval-Augmented Generation (RAG). The application allows users to upload PDF documents and ask contextual questions about their content using semantic search and a locally deployed language model.

Project Overview

This project demonstrates how modern AI systems combine document parsing, text chunking, embedding generation, vector similarity search, and local large language model integration.

The system retrieves relevant document sections using FAISS vector search and generates grounded answers using the Phi model via Ollama.

It is designed as a placement-ready AI systems prototype.

System Architecture

User uploads a PDF document.

The document text is cleaned and split into smaller chunks.

Sentence-transformer embeddings are generated for each chunk.

Embeddings are stored in a FAISS vector database.

When a user asks a question:

The query is embedded.

Top relevant chunks are retrieved.

Retrieved context is passed to the local LLM.

The Phi model generates a contextual answer based only on retrieved information.

Tech Stack

Python
Streamlit
LangChain
FAISS (Vector Database)
Sentence Transformers
Ollama
Phi Model

Setup Instructions

Clone the repository:
git clone https://github.com/Shreya59422/PDF-Search-and-QA.git

Install Python dependencies:
pip install -r requirements.txt

Install Ollama from:
https://ollama.com/download

Verify installation:
ollama --version

Pull the Phi model:
ollama pull phi

Run the application:
streamlit run app.py

Features

Upload any PDF document
Semantic chunk-based retrieval
Vector similarity search using FAISS
Context-grounded answer generation
Chat-style interface
Fully offline execution
Privacy-focused design

Limitations

Performance depends on CPU capability
Smaller local models may generate shorter answers
Designed as a prototype demonstration
Not optimized for large-scale production deployment

Purpose

This project demonstrates practical implementation of Retrieval-Augmented Generation (RAG) architecture for document intelligence systems. It showcases embedding-based semantic search, vector database integration, context-aware answer generation, and offline AI deployment trade-offs.
