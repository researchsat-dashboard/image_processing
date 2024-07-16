import os
import boto3

ACCESS_KEY=""
SECRET_KEY=""

def upload_s3_bucket():
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    bucket_name = ''
    directory = ""
    for root, _, files in os.walk(directory):
        for file in files:
            complete_file_path = os.path.join(root, file)
            s3.upload_file(complete_file_path, bucket_name, file)


upload_s3_bucket()