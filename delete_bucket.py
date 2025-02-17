import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set the bucket name
bucket_name = 'my-boto3-s3-bucket-sahil'  # Ensure this matches your bucket name

def empty_bucket(bucket_name):
    """
    Deletes all objects (including versioned objects if versioning is enabled) before deleting the bucket.
    """
    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted {obj['Key']}")

        # If versioning is enabled, delete all versions
        versions = s3.list_object_versions(Bucket=bucket_name)
        if 'Versions' in versions:
            for version in versions['Versions']:
                s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
                print(f"Deleted version {version['VersionId']} of {version['Key']}")

        print("Bucket emptied successfully!")
    except Exception as e:
        print(f"Error emptying bucket: {e}")

try:
    # Empty the bucket first
    empty_bucket(bucket_name)

    # Delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} deleted successfully!')

except Exception as e:
    print(f"Error deleting bucket: {e}")
