import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os

def get_s3_client(access_key, secret_key):
    try:
        # Create an S3 client using provided credentials
        s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        return s3_client
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise ValueError(f"Invalid AWS credentials: {e}")

def list_buckets(s3_client):
    try:
        response = s3_client.list_buckets()
        return response['Buckets']
    except Exception as e:
        raise ValueError(f"Error listing buckets: {e}")
