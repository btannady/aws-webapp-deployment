import boto3

# Initialize an AWS S3 client.
s3: boto3.client = boto3.client('s3')

# List all existing S3 buckets.
print("List of Buckets:")
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
