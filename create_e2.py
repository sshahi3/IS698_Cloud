# Initialize a session using Boto3
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-085ad6ae776d8f09c',  # Amazon Linux 2 AMI (Free Tier Eligible)
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='lab2c',  # Ensure you have created this key pair
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyPythonEC2Instance'}
            ]
        }
    ]
)

print(f'Created instance with ID: {instance[0].id}')
