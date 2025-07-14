import json
from langchain_community.vectorstores import FAISS
from chatbot.config import * 
# from langchain_openai import OpenAIEmbeddings
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

from pathlib import Path

def load_products(filepath="api/utils/products.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def build_vector_store(products):
    docs = []
    for product in products:
        content = f"{product['title']}\n\n{product['description']}"
        metadata = {"source": product["url"]}
        docs.append(Document(page_content=content, metadata=metadata))

    # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("api/utils/faiss_index")
    print(f"✅ Ingested {len(docs)} products into vector store.")

if __name__ == "__main__":
    products = load_products()
    build_vector_store(products)
