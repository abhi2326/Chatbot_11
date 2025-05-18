# AI Chatbot Web Scraper

## Description
A Streamlit-based chatbot that scrapes website content using Playwright and answers questions using a Hugging Face-hosted LLM (Mistral-7B-Instruct).

## Setup & Deployment (Streamlit Cloud)

1. Upload this project to a GitHub repository.
2. Set the following environment variable in Streamlit Cloud:
   - `HUGGINGFACEHUB_API_TOKEN=
3. Add the following commands to install:
   ```
   pip install -r requirements.txt
   python -m playwright install
   ```
4. Main entry point:
   ```
   streamlit run app.py
   ```

## Features
- Scrapes dynamic web content using Playwright
- Processes and chunks text for better context
- Answers user questions based only on scraped content
- Chat history and user interaction in Streamlit

✅ No further setup required.