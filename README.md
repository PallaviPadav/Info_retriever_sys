# Information Retriever System 📝

An AI-powered PDF Question Answering System built using Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Groq LLM.

The application allows users to upload PDF documents and ask questions related to the uploaded content using Conversational AI and Retrieval-Augmented Generation (RAG).

---

# Features 🚀

- Upload multiple PDF documents
- Extract text from PDFs
- Split documents into chunks
- Generate vector embeddings using Hugging Face
- Store embeddings in FAISS vector database
- Conversational Retrieval Chain using LangChain
- Context-aware question answering
- Chat history memory support
- Highlighted user and AI chat interface
- Latest responses displayed at the top

---

# Tech Stack 🛠️

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Groq LLM
- PyPDF2

---

# Project Structure 📂

```bash
Info_Retriever_System/
│
├── app.py
├── requirements.txt
├── .env
│
├── info_retriever/
│   ├── __init__.py
│   └── helper.py
│
└── README.md
```

---

# Installation ⚙️

## Clone the Repository

```bash
git clone <your_repository_url>
cd Info_Retriever_System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables 🔑

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

# Running the Application ▶️

```bash
streamlit run app.py
```

---

# How It Works ⚡

## 1. PDF Upload

Users upload one or multiple PDF files through the Streamlit sidebar.

## 2. Text Extraction

The application extracts text from PDFs using PyPDF2.

## 3. Text Chunking

The extracted text is split into smaller chunks using RecursiveCharacterTextSplitter.

## 4. Embedding Generation

Text chunks are converted into vector embeddings using HuggingFaceEmbeddings.

## 5. Vector Storage

Embeddings are stored in a FAISS vector database for efficient similarity search.

## 6. Conversational Retrieval

When the user asks a question:

- Relevant chunks are retrieved from FAISS
- The retrieved context is passed to Groq LLM
- The model generates context-aware answers

## 7. Memory Support

ConversationBufferMemory stores previous conversations to maintain chat context.

---

# Main Components 📌

## app.py

Handles:

- Streamlit UI
- PDF upload
- User interactions
- Chat history display

## helper.py

Contains utility functions for:

- PDF text extraction
- Chunk creation
- Vector store generation
- Conversational chain setup

---

# Libraries Used 📚

```python
streamlit
langchain
langchain-community
langchain-groq
langchain-huggingface
faiss-cpu
PyPDF2
python-dotenv
```

---

# Sample Workflow 🔄

1. Upload PDF files
2. Click "Submit and Process"
3. Ask questions related to the PDF
4. Get AI-generated contextual answers

---

# Example Questions 💡

- What is machine learning?
- Summarize the uploaded document
- Explain the introduction section
- What are the key findings?

---

# Future Improvements 🚀

- PDF citation support
- Chat export functionality
- Voice input support
- Multi-language support
- Database integration
- Authentication system
- Streaming responses
- Dark mode UI

---

# Author ✨

Developed using:

- Streamlit
- LangChain
- Groq LLM
- Hugging Face Embeddings

---

# License 📄

This project is open-source and available under the MIT License.
