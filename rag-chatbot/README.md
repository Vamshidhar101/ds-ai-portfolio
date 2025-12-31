# 🤖 RAG Document Chatbot
## Project Overview
This tool allows users to upload confidential PDF documents and query them using Natural Language. It utilizes **Retrieval-Augmented Generation (RAG)** to ensure answers are based strictly on the uploaded content, minimizing hallucinations.

## Tech Stack
* **Frontend:** Streamlit
* **LLM:** GPT-4 (via OpenAI API)
* **Vector DB:** FAISS
* **Orchestration:** LangChain

## How to Run
1. `pip install -r requirements.txt`
2. `streamlit run app.py`