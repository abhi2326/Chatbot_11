from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings()
    vectordb = FAISS.from_documents(docs, embeddings)
    return vectordb

def get_retriever(vectordb):
    return vectordb.as_retriever(search_kwargs={'k': 5})