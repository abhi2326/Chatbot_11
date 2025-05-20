from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

# Initialize the language model
llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1", model_kwargs={"temperature": 0.2})

# Function to get response from the QA chain
def get_chat_response(question, retriever):
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.invoke({"query": question})
