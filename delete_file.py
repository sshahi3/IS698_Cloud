import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set bucket and file names
bucket_name = 'my-boto3-s3-bucket-sahil'  # Ensure this matches your bucket name
file_name = 'myfile.txt'

try:
    # Delete the file from S3
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    print(f'File {file_name} deleted successfully from {bucket_name}!')
except Exception as e:
    print(f"Error deleting file: {e}")
