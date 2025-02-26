import boto3
import json
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_OBJECT_KEY = os.getenv("AWS_OBJECT_KEY")

def get_products_from_s3():
    """Busca e retorna os dados dos produtos armazenados no S3"""
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    s3 = session.client("s3")
    
    obj = s3.get_object(Bucket=AWS_BUCKET_NAME, Key=AWS_OBJECT_KEY)
    data = json.loads(obj["Body"].read().decode("utf-8"))
    
    return data
