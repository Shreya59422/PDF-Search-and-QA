import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import ollama

st.set_page_config(page_title="Private PDF Chat Assistant")
st.title("📄 Private Offline PDF Chat Assistant (Fast Version)")

# ------------------------
# Session State
# ------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------
# Upload PDF
# ------------------------
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and st.session_state.vectorstore is None:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    # Clean text
    for doc in documents:
        doc.page_content = doc.page_content.replace("\n", " ")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,   # smaller chunks = faster retrieval
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    st.session_state.vectorstore = vectorstore

    st.success("PDF processed successfully!")

# ------------------------
# Chat Interface
# ------------------------
if st.session_state.vectorstore:

    user_input = st.chat_input("Ask a question about the document")

    if user_input:

        # Limit retrieval to reduce CPU load
        retrieved_docs = st.session_state.vectorstore.similarity_search(user_input, k=2)
        context = " ".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{user_input}

Answer briefly:
"""

        # ⚡ Fast generation settings
        response = ollama.chat(
            model="phi",
            messages=[{"role": "user", "content": prompt}],
            options={
                "num_predict": 80,   # limit answer length
                "temperature": 0.3
            }
        )

        answer = response["message"]["content"]

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", answer))

    # Display chat history
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)
