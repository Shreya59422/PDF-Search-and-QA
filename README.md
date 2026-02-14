**PDF-Search-and-QA**

PDF-Search-and-QA is a document question-answering system built using Retrieval-Augmented Generation (RAG). The application allows users to upload PDF documents and ask contextual questions about their content using semantic search and a locally deployed language model.

**Project Overview**

This project demonstrates how modern AI systems combine document parsing, text chunking, embedding generation, vector similarity search, and local large language model integration.
The system retrieves relevant document sections using FAISS vector search and generates grounded answers using the Phi model via Ollama.

**System Architecture**

1. User uploads a PDF document.

2. The document text is cleaned and split into smaller chunks.

3. Sentence-transformer embeddings are generated for each chunk.

4. Embeddings are stored in a FAISS vector database.

5. When a user asks a question:

- The query is embedded.

- Top relevant chunks are retrieved.

- Retrieved context is passed to the local LLM.

6. The Phi model generates a contextual answer based only on retrieved information.

**Tech Stack**

Python
Streamlit
LangChain
FAISS (Vector Database)
Sentence Transformers
Ollama
Phi Model

**Setup Instructions**

1. Clone the repository:
git clone https://github.com/Shreya59422/PDF-Search-and-QA.git

2. Install Python dependencies:
pip install -r requirements.txt

3. Install Ollama from:
https://ollama.com/download

4. Verify installation:
ollama --version

5. Pull the Phi model:
ollama pull phi

6. Run the application:
streamlit run app.py

**Features**

1. Upload any PDF document
2. Semantic chunk-based retrieval
3. Vector similarity search using FAISS
4. Context-grounded answer generation
5. Chat-style interface
6. Fully offline execution
7. Privacy-focused design

**Limitations**

1. Performance depends on CPU capability
2. Smaller local models may generate shorter answers
3. Designed as a prototype demonstration
4. Not optimized for large-scale production deployment

**Purpose**

This project demonstrates practical implementation of Retrieval-Augmented Generation (RAG) architecture for document intelligence systems. It showcases embedding-based semantic search, vector database integration, context-aware answer generation, and offline AI deployment trade-offs.


