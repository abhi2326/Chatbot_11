from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

def process_text(text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]