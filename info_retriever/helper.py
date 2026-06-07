import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import ConversationalRetrievalChain
#from langchain.memory import ConversationBufferMemory
from langchain_classic.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embedding = HuggingFaceEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding = embedding)
    return vector_store

def get_conversational_chain(vector_store):

    llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(llm = llm, retriever=retriever,memory=memory)
    return qa_chain
    
   