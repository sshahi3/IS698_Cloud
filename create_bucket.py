import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define a unique bucket name
bucket_name = 'my-boto3-s3-bucket-sahil'  # Ensure this is globally unique

# Create the S3 bucket
response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created successfully!')
