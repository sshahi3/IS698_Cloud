import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set bucket and file names
bucket_name = 'my-boto3-s3-bucket-sahil'  # Ensure this matches your bucket name
file_name = 'myfile.txt'
download_name = 'downloaded-file.txt'

try:
    # Download the file from S3
    s3.download_file(bucket_name, file_name, download_name)
    print(f'File {file_name} downloaded successfully as {download_name}!')
except Exception as e:
    print(f"Error downloading file: {e}")
