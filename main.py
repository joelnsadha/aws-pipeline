import boto3
from dotenv import load_dotenv
import os


# Load env variables
load_dotenv()
upload_file = os.getenv("CIRCUITS")

# List bicket names
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)

try:
    # Upload to s3 bucket
    s3.meta.client.upload_file(upload_file, "f1-demo-bucket", "f1-data/circuits")
except Error as e:
    print("Error uploading", e)
