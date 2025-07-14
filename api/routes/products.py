from fastapi import APIRouter, Query
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
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

        # Load vector DB and embedding
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

        # LLM setup using HuggingFace GPT-2
        local_llm_pipeline = pipeline(
            "text-generation",
            model="gpt2",
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True
        )
        llm = HuggingFacePipeline(pipeline=local_llm_pipeline)

        # Get relevant documents
        retriever = db.as_retriever()
        docs = retriever.get_relevant_documents(query)
        if not docs:
            return {"query": query, "answer": "Sorry, I couldn't find any relevant products."}

        # Custom prompt template
        custom_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
Use the following context to answer the question concisely and helpfully.

{context}

Question: {question}
Answer:"""
        )

        # RetrievalQA chain with custom prompt
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False,
            chain_type_kwargs={"prompt": custom_prompt}
        )

        result = qa_chain.run(query)
        return {"query": query, "answer": result}

    except Exception as e:
        return {"error": str(e)}
