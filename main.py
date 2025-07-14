from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.routes import products
from api.routes import outlets

app = FastAPI(
    title="ZUS Coffee Chatbot API",
    description="RAG-based endpoints for ZUS Drinkware & Outlets",
    version="1.0.0"
)

app.include_router(products.router, prefix="/api", tags=["Products"])
app.include_router(outlets.router, prefix="/api", tags=["Outlets"])

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h2>✅ ZUS Coffee Chatbot API is Running!</h2>
    <p>Use the endpoints:</p>
    <ul>
        <li><code>/api/products?query=your+question</code></li>
        <li><code>/api/outlets?query=your+question</code></li>
    </ul>
    """
