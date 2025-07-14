# 🧠 AdlynKhairudin\_Mindhive\_Chatbot

Custom RAG-based Chatbot using FastAPI for ZUS Coffee use case.

---

## 🚀 Project Structure

```
AdlynKhairudin_Mindhive_Chatbot/
├── api/
│   ├── main.py                  # FastAPI app entry point
│   ├── routes/
│   │   ├── products.py         # /products?query=...
│   │   └── outlets.py          # /outlets?query=...
│   └── utils/
│       ├── ingest_products.py  # Vector store ingestion script
│       └── scrape_outlets.py   # Scraper to populate SQLite DB
├── chatbot/
│   └── config.py               # API keys or env vars
├── api/utils/
│   ├── faiss_index/            # Saved vectorstore index
│   └── outlets.db              # SQLite DB with outlet info
├── test_chatbot.py             # Sample test script to query endpoints
├── requirements.txt
└── README.md
```

---

## 📦 Setup Instructions

### 1. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install these manually:

```bash
pip install fastapi uvicorn langchain openai transformers sentence-transformers sqlite-utils requests
```

---

## 🛠️ Preprocessing

### ✅ Ingest Products into Vector Store

```bash
python api/utils/ingest_products.py
```

Stores `products.json` data as a FAISS vector index in `api/utils/faiss_index/`

### ✅ Scrape and Save Outlets into SQLite

```bash
python api/utils/scrape_outlets.py
```

Creates/updates `api/utils/outlets.db` containing outlet information.

---

## ⚡ Run FastAPI Server

```bash
uvicorn api.main:app --reload
```

Visit docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 Test API Endpoints

### Use Postman or Browser:

* `GET /products?query=Do you have a ZUS tumbler?`
* `GET /outlets?query=List all outlets in Selangor`

### Or Run:

```bash
python test_chatbot.py
```

---

## ✅ Deliverables Checklist

* [x] `/products` vector search endpoint (RAG)
* [x] `/outlets` Text2SQL endpoint using SQLite
* [x] Ingestion scripts for vector store & SQLite
* [x] Working FastAPI server with both endpoints
* [x] Sample test script and transcripts showing success/failure

---

## 📎 Sample Queries

### /products

```
Query: Do you have a ZUS tumbler?
Answer: Yes, we do. [summary with matching drinkware info]
```

### /outlets

```
Query: List all outlets in Selangor
Answer: Table or list of all ZUS Coffee outlets in Selangor
```

---

## 🙋 FAQ

**Q: I get 'no such table: outlets'?**
A: Run `scrape_outlets.py` to generate the `outlets.db`.

**Q: I get FAISS load errors?**
A: Ensure `faiss_index/` exists by running `ingest_products.py`

**Q: I get prompt or token length warnings?**
A: Use `max_new_tokens` instead of `max_length` for better control.

---

## 🧠 Tech Stack

* FastAPI
* FAISS
* HuggingFace Transformers
* SQLite
* LangChain

---

## 👩‍💻 Author

Adlyn Khairudin – Mindhive Chatbot Technical Assessment
