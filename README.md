## **AWS S3 File Upload**

**Prerequisites**
Before running the program, ensure you have:

- Python installed on your machine
- AWS account with access to S3
- Access key ID and secret access key for AWS credentials

**Installation**

1. Clone this repository to your local machine:

`git clone <repository_url>`

2. Install the required Python packages using pip:

`pip install boto3 python-dotenv`

3. Create a .env file in the project directory and add your AWS credentials:

`AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
CIRCUITS=file_path_to_upload`

Replace your_access_key_id, your_secret_access_key, and file_path_to_upload with your AWS credentials and the path of the file you want to upload.

**Usage**
Run the Python script upload_to_s3.py:

`python upload_to_s3.py`

This will upload the specified file to the configured S3 bucket.

**Configuration**
Modify the .env file to change the file path or destination bucket.
