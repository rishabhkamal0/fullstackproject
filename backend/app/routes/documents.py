from fastapi import APIRouter, UploadFile, File, Query
from app.services.storage_service import upload_to_s3
from app.services.search_service import index_document, search_documents
from app.utils.parsers import parse_document_content
from app.models.database import SessionLocal
from app.models.document import Document

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    parsed_content = parse_document_content(content, file.filename)

    # Upload to S3
    s3_url = upload_to_s3(file.filename, content)

    # Index in Elasticsearch
    index_document(file.filename, parsed_content)

    # Save to the database
    db = SessionLocal()
    new_document = Document(filename=file.filename, s3_url=s3_url)
    db.add(new_document)
    db.commit()
    db.close()

    return {"message": "File uploaded successfully", "s3_url": s3_url}

@router.get("/query/")
async def query_documents(q: str = Query(...)):
    results = search_documents(q)
    return {"query": q, "results": results}
