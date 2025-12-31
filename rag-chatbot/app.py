import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# Page Config
st.set_page_config(page_title="Corporate Doc Chatbot", layout="wide")

st.title("🤖 AI Document Assistant (RAG Pipeline)")
st.markdown("Upload a PDF policy document and ask questions about it.")

# API Key Input (For Security)
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

# File Uploader
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file and api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    
    # Save file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Indexing document..."):
        # Loader & Embeddings
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load_and_split()
        embeddings = OpenAIEmbeddings()
        
        # Vector Store (FAISS)
        vectorstore = FAISS.from_documents(pages, embeddings)
        retriever = vectorstore.as_retriever()
        
        # Chain
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-4", temperature=0),
            chain_type="stuff",
            retriever=retriever
        )
        st.success("Document Indexed Successfully!")

    # Chat Interface
    query = st.text_input("Ask a question about the document:")
    if query:
        response = qa.run(query)
        st.write("### Answer:")
        st.write(response)

else:
    st.info("Please enter an API key and upload a document to start.")