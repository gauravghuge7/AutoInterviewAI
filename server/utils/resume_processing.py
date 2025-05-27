# utils/resume_processing.py
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
import numpy as np

def parse_resume(file_path):
    reader = PdfReader(file_path)
    full_text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    return full_text

def embed_text(text):
    from openai import OpenAI
    client = OpenAI("OPENAI_API_KEY")
    response = client.embeddings.create(
        input=text,               # no need for a list, unless batching
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

