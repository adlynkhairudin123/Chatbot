from fastapi import FastAPI
from api.routes import products
from api.routes import outlets

app = FastAPI(
    title="ZUS Coffee Chatbot API",
    description="RAG-based endpoints for ZUS Drinkware & Outlets",
    version="1.0.0"
)

# Register routes
app.include_router(products.router, prefix="/api", tags=["Products"])
app.include_router(outlets.router, prefix="/api", tags=["Outlets"])
