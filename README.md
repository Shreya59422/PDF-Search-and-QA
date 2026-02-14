\# 🔒 Private Offline PDF RAG Assistant



A Retrieval-Augmented Generation (RAG) based AI assistant that allows users to upload PDF documents and ask contextual questions about them.



\##  Features



\- Upload PDF documents

\- Semantic chunking and embedding generation

\- Vector search using FAISS

\- Context-grounded answer generation

\- Chat-style interface

\- Fully offline execution using Ollama (Phi model)



\##  Architecture



1\. PDF uploaded and parsed using PyPDFLoader.

2\. Text cleaned and split into chunks.

3\. Embeddings generated using sentence-transformers.

4\. Chunks stored in FAISS vector database.

5\. User query retrieves top relevant chunks.

6\. Retrieved context injected into local LLM (Phi).

7\. Model generates grounded answer.



\##  Tech Stack



\- Python

\- Streamlit

\- LangChain

\- FAISS

\- Sentence Transformers

\- Ollama (Phi)



\## How To Run



Install dependencies:



pip install -r requirements.txt



Install Ollama:

https://ollama.com/download



Pull model:



ollama pull phi



Run:



streamlit run app.py



\##  Note



Designed as a privacy-focused document intelligence system demonstrating real-world RAG architecture.



