import os
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY="insert key here"
SECRET_KEY="insert key here"

def download_s3_bucket(bucket_name):
    # Initialize the S3 client with credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']
        script_directory = os.path.dirname(os.path.realpath(__file__))
        download_folder = os.path.join(script_directory, bucket_name)
        # Create a folder named after the bucket
        os.makedirs(download_folder, exist_ok=True)
        for obj in objects:
            # Get the key (path) of the object
            key = obj['Key']
            # Skip if the object is a directory
            if key.endswith('/'):
                continue
            # Create the local directory structure if it doesn't exist
            local_path = os.path.join(download_folder, key)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            # Download the object
            s3.download_file(bucket_name, key, local_path)
            print(f'Downloaded: {key}')
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    # Replace 'your_bucket_name' with the name of your S3 bucket
    bucket_name = 'bucket name here'
    download_s3_bucket(bucket_name)