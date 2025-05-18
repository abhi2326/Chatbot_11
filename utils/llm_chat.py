from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1", model_kwargs={"temperature":0.2})

def get_chat_response(question, retriever):
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(question)