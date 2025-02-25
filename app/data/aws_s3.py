import boto3
import json

AWS_ACCESS_KEY = "AKIAW5WU45WLGEZTT3UC"
AWS_SECRET_KEY = "zi9W3b9hVhTuofZAoDRI/PmHN3P6YX/inqBdBP8S"
AWS_BUCKET_NAME = "datalake-fakestore"
AWS_OBJECT_KEY = "products_data.json"

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
