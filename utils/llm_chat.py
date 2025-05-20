from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

# Initialize the language model
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    model_kwargs={"temperature": 0.2}
)

# Function to get response from the QA chain
def get_chat_response(question, retriever):
    # Use chain_type="stuff" (can also use "map_reduce", etc. depending on needs)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # default and simplest
        return_source_documents=True  # optional, good for transparency
    )

    result = qa_chain({"query": question})
    return result
