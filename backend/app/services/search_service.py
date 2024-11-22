from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Elasticsearch URL and credentials from environment variables
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Initialize the Elasticsearch client
es = Elasticsearch(
    [ELASTICSEARCH_URL],  # URL should be passed as a list
    basic_auth=(USERNAME, PASSWORD) if USERNAME and PASSWORD else None
)

# Test the connection
if es.ping():
    print("Elasticsearch connected successfully!")
else:
    print("Failed to connect to Elasticsearch.")
