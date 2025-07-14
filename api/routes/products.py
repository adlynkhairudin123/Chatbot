from fastapi import APIRouter, Query
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

DB_PATH = "api/utils/faiss_index"

router = APIRouter()

@router.get("/products")
async def query_products(query: str = Query(..., description="User question about ZUS Drinkware")):
    try:
        if not query.strip():
            return {"error": "Empty query provided."}
        
        if "crash" in query.lower():
            raise RuntimeError("Simulated server crash")

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

        local_llm_pipeline = pipeline(
            "text-generation",
            model="gpt2",
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True
        )
        llm = HuggingFacePipeline(pipeline=local_llm_pipeline)
        retriever = db.as_retriever()

        docs = retriever.get_relevant_documents(query)
        if not docs:
            return {"query": query, "answer": "Sorry, I couldn't find any relevant products."}

        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        result = qa_chain.run(query)
        return {"query": query, "answer": result}

    except Exception as e:
        return {"error": str(e)}
