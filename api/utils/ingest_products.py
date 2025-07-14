import json
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document

# Load product data
with open("api/utils/products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create documents for embedding
documents = []
for item in data:
    text = f"{item['title']}. {item['description']}"
    documents.append(Document(page_content=text, metadata={"title": item["title"]}))

# Create embeddings
embeddings = OpenAIEmbeddings()

# Build and save FAISS vector store
db = FAISS.from_documents(documents, embeddings)
db.save_local("api/vectorstore/products_faiss")

print("✅ Product vector store built and saved.")
