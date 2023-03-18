import streamlit as st
import requests
import PyPDF2
import docx2txt
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()
    return text

def read_docx(file):
    return docx2txt.process(file)

def read_text_file(file):
    return file.read()

def summarize_text(text):
    # System message containing instructions
    system_string = "you are a helpful assistant. you help summarize text; the summarization must be in bullet point. the summarization shall be in Chinese; of length 1/4 of the original article. try to keep all the numbers; they are very important! do not simply shorten each sentence. try to understand the entire paragraph and provide a coherent summary."

    # User message with input text from the form
    user_string = f"please help me summarize the below text; the summarization must be in bullet point. the summarization shall be in Chinese; of length 1/4 of the original article. try to keep all the numbers; they are very important! do not simply shorten each sentence. try to understand the entire paragraph and provide a coherent summary. {text}"

    # API request data
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_string},
            {"role": "user", "content": user_string},
        ]
    }

    # API endpoint URL
    url = 'https://api.openai.com/v1/chat/completions'

    API_KEY = os.getenv("OPENAI_API_KEY")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # Make API request
    response = requests.post(url, json=data, headers=headers)
    
    # Get response text from API response
    response_text = response.json()['choices'][0]['message']['content']

    return response_text

# Streamlit app
def app():
    st.title("ChatGPT Text Summarization")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF or Word document", type=["pdf", "docx", "txt"])

    # Input form
    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            text = read_pdf(uploaded_file)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = read_docx(uploaded_file)
        elif file_type == "text/plain":
            text = read_text_file(uploaded_file)
        else:
            st.error("Unsupported file type")
            return
        st.text_area("Enter your text here", value=text, height=200)
    else:
        text = st.text_area("Enter your text here", height=200)

    # Submit button
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
            # Display output
            st.markdown(summary, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
