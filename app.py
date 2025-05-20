import streamlit as st
import os
import subprocess  # To install Playwright browsers if needed

# Automatically install Playwright browsers (if you haven't done this before)
subprocess.run(["playwright", "install"], check=True)

from scraper.static_scraper import scrape_static
from scraper.dynamic_scraper import scrape_dynamic
from utils.text_processor import process_text
from utils.retriever import get_vectorstore, get_retriever
from utils.llm_chat import get_chat_response

# Ensure 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

st.set_page_config(page_title="AI Web Chatbot", layout="wide")
st.title("AI-Powered Website Chatbot")

url = st.text_input("Enter Website URL")
mode = st.radio("Select Scraping Mode", ["Static", "JavaScript-heavy"])

if st.button("Scrape and Load"):
    with st.spinner("Scraping content..."):
        if mode == "Static":
            raw_content = scrape_static(url)
        else:
            raw_content = scrape_dynamic(url)

        with open("data/scraped_content.txt", "w", encoding="utf-8") as f:
            f.write(raw_content)

        # Process text and create vectorstore & retriever
        docs = process_text(raw_content)
        vectordb = get_vectorstore(docs)
        st.session_state.retriever = get_retriever(vectordb)
        st.success("Scraping and processing done!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if prompt := st.chat_input("Ask something about the website"):
    if "retriever" in st.session_state:
        st.chat_message("user").write(prompt)
        # Updated get_chat_response call with correct signature:
        response = get_chat_response(prompt, st.session_state.retriever)
        st.chat_message("assistant").write(response)
        st.session_state.chat_history.append((prompt, response))
    else:
        st.warning("Please scrape a website first.")

if st.button("Download Chat Log"):
    with open("data/chat_log.txt", "w", encoding="utf-8") as f:
        for q, a in st.session_state.chat_history:
            f.write(f"User: {q}\nBot: {a}\n\n")
    st.download_button("Download Chat Log", open("data/chat_log.txt", "rb"), file_name="chat_log.txt")
