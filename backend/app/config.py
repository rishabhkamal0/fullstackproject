from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now you can access the variables using os.getenv()
DATABASE_URL = os.getenv("DATABASE_URL")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_REGION = os.getenv("S3_REGION")
ELASTICSEARCH_URL = os.getenv("http://localhost:9200")
