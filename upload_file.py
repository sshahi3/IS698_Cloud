import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set bucket name (ensure it matches your created bucket)
bucket_name = 'my-boto3-s3-bucket-sahil'

# File details
file_name = 'myfile.txt'

# Create a sample text file
with open(file_name, 'w') as f:
    f.write("Hello S3")

# Upload the file to the S3 bucket
s3.upload_file(file_name, bucket_name, file_name)

print(f'File {file_name} uploaded successfully to {bucket_name}!')
