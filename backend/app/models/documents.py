from sqlalchemy import Column, Integer, String
from .database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    s3_url = Column(String, nullable=False)
