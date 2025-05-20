from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Initialize Zephyr-7B-Beta LLM once (reuse it)
llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    model_kwargs={
        "temperature": 0.3,
        "max_new_tokens": 512,
        "top_k": 50,
        "repetition_penalty": 1.1,
    }
)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
<|system|>
You are a helpful, honest, and concise assistant.
Use the following context to answer the user's question.
If you don’t know the answer, say "I don't know" and do not make up facts.
</s>
<|user|>
Context:
{context}

Question:
{question}
</s>
<|assistant|>
"""
)

def get_chat_response(question, retriever):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=False
    )
    # Use invoke with key "query" as expected
    result = qa_chain.invoke({"query": question})
    return result["result"]
