import boto3
from app.config import S3_BUCKET_NAME, S3_REGION

s3_client = boto3.client('s3')

def upload_to_s3(filename: str, content: bytes) -> str:
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=filename, Body=content)
    return f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{filename}"
