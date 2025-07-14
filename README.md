## ✅ Part 1: GitHub Repository (Public, No Secrets)

* **Repo URL**:
  👉 [https://github.com/adlynkhairudin123/Chatbot](https://github.com/adlynkhairudin123/Chatbot)

* `.env` file is **excluded** using `.gitignore`.

---

## ✅ Part 2: Hosted Demo (Render)

* **Render URL (Live API)**:
  👉 [https://adlyns-mindhive-chatbot.onrender.com](https://adlyns-mindhive-chatbot.onrender.com)

* Available endpoints:

  * `/api/products?query=your+question`
  * `/api/outlets?query=your+question`

---

## ✅ Part 3: README.md (Add this to your repo root)

````markdown
# 🧠 ZUS Coffee Chatbot (Mindhive Technical Assessment)

A FastAPI-based chatbot that provides:
- Product recommendations using Retrieval-Augmented Generation (RAG)
- Outlet information using Text-to-SQL (SQLite)
- Memory-enabled local chatbot conversation

Hosted on Render: [Live API](https://adlyns-mindhive-chatbot.onrender.com)

---

## 🚀 Setup & Run Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/adlynkhairudin123/Chatbot
   cd Chatbot
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI app**

   ```bash
   uvicorn main:app --reload --port 10000
   ```

4. **Access endpoints**

   * [http://127.0.0.1:10000/api/products?query=Do+you+have+ZUS+tumbler](http://127.0.0.1:10000/api/products?query=Do+you+have+ZUS+tumbler)
   * [http://127.0.0.1:10000/api/outlets?query=Outlets+in+Selangor](http://127.0.0.1:10000/api/outlets?query=Outlets+in+Selangor)?

---

## 🧱 Architecture Overview

### Main Features:

* `FastAPI` backend for API routing
* `LangChain` for both:

  * RAG (Product Q\&A via FAISS + local LLM)
  * Text2SQL for outlet queries on SQLite
* Local LLM: `sshleifer/tiny-gpt2` via HuggingFace
* Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
* Memory-based CLI chatbot (`part1_seqConv.py`)

### Key Trade-offs:

* 🧠 Local LLMs are lightweight but less powerful than cloud APIs
* 🪄 SQLite is used for simplicity (for demo purposes)
* 🏗️ Modular code for each chatbot component

````

---

## ✅ Part 4: Documentation (Add this to `/docs/API.md`)

```markdown
# 📚 API Specification

## 🔹 GET /api/products

**Description**: RAG-based endpoint using FAISS + LLM

**Query Params**:
- `query` (str): A user question about ZUS drinkware

**Example**:
````

GET /api/products?query=Do you have ZUS tumbler

````

**Response**:
```json
{
  "query": "Do you have ZUS tumbler",
  "answer": "Yes, we offer the ZUS All-Can Tumbler and other options."
}
````

---

## 🔹 GET /api/outlets

**Description**: Text-to-SQL endpoint using SQLite

**Query Params**:

* `query` (str): Question about outlet count, location, etc.

**Examples**:

```
GET /api/outlets?query=How many outlets?
GET /api/outlets?query=Outlets in Selangor?
```

**Response**:

```json
{
  "query": "Outlets in Selangor?",
  "results": [
    {
      "id": 1,
      "name": "ZUS Coffee – Subang Jaya",
      "state": "Kuala Lumpur / Selangor",
      ...
    }
  ]
}
```

---

## 💥 Error Handling

| Error                  | Response                               |
| ---------------------- | -------------------------------------- |
| Missing query param    | `{"error": "Empty query provided."}`   |
| SQL injection detected | `{"error": "Invalid input detected."}` |
| Internal errors        | `{"error": "Server error: ... "}`      |

```

---

## ✅ Part 5: Flow Diagrams / Screenshots

### 🧭 High-Level Flow Diagram

```

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/e9d75ab9-72b2-4842-83d8-ea39f641c02b" />


````

---

### 🖼️ Screenshot:
Part 1: <img width="1612" height="300" alt="Screenshot 2025-07-14 224531" src="https://github.com/user-attachments/assets/c96dda84-1170-4999-b011-70bf8944f983" />

Part 2: <img width="1145" height="309" alt="Screenshot 2025-07-14 225712" src="https://github.com/user-attachments/assets/be22102e-79fd-418e-aacc-698b65db53dd" />

Part 3: <img width="1177" height="383" alt="Screenshot 2025-07-14 225918" src="https://github.com/user-attachments/assets/5d263011-aee1-4dc3-a631-23dd78c004b9" />

```plaintext
✅ ZUS Coffee Chatbot API is Running!

Use the endpoints:

  /api/products?query=your+question
  /api/outlets?query=your+question
````

---

