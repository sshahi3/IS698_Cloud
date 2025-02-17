import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set bucket name (ensure it matches your created bucket)
bucket_name = 'my-boto3-s3-bucket-sahil'

try:
    # Enable versioning on the bucket
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f'Versioning enabled for bucket {bucket_name}!')
except Exception as e:
    print(f"Error enabling versioning: {e}")
