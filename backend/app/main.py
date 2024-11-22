from fastapi import FastAPI
from app.routes import documents

app = FastAPI()

# Include routes for document operations
app.include_router(documents.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the document query backend!"}
