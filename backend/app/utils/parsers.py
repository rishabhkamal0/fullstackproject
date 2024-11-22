import os
from typing import Union
from PyPDF2 import PdfReader
from docx import Document

def parse_document_content(content: bytes, filename: str) -> str:
    """
    Parses and extracts text from supported file formats.

    Args:
        content (bytes): File content as bytes.
        filename (str): Name of the file.

    Returns:
        str: Extracted text content.
    """
    file_ext = os.path.splitext(filename)[1].lower()

    if file_ext == ".pdf":
        return extract_text_from_pdf(content)
    elif file_ext == ".docx":
        return extract_text_from_docx(content)
    else:
        raise ValueError(f"Unsupported file type: {file_ext}")

def extract_text_from_pdf(content: bytes) -> str:
    """
    Extract text from a PDF file.

    Args:
        content (bytes): PDF content as bytes.

    Returns:
        str: Extracted text.
    """
    with open("temp.pdf", "wb") as temp_pdf:
        temp_pdf.write(content)

    text = ""
    try:
        reader = PdfReader("temp.pdf")
        for page in reader.pages:
            text += page.extract_text() or ""
    finally:
        os.remove("temp.pdf")  # Clean up the temporary file

    return text

def extract_text_from_docx(content: bytes) -> str:
    """
    Extract text from a DOCX file.

    Args:
        content (bytes): DOCX content as bytes.

    Returns:
        str: Extracted text.
    """
    with open("temp.docx", "wb") as temp_docx:
        temp_docx.write(content)

    text = ""
    try:
        doc = Document("temp.docx")
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    finally:
        os.remove("temp.docx")  # Clean up the temporary file

    return text
