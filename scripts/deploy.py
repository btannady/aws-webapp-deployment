import boto3
from datetime import datetime
import os

class S3Manager:
    def __init__(self):
        self.S3_BUCKET_NAME = "aws-webapp-deployment-bucket-2025"
        self.s3: boto3.client = boto3.client('s3')  # Initialize an AWS S3 client.

    def s3_sanity_check(self):
        ''' Ensure the targeted S3 bucket exists, otherwise raise exception.'''
        try:
            print(f"Starting Sanity Check for S3 Bucket'{self.S3_BUCKET_NAME}'.")
            self.s3.head_bucket(Bucket=self.S3_BUCKET_NAME)
            print(f"Detected S3 Bucket'{self.S3_BUCKET_NAME}'.")
        except Exception as e:
            print(f"SanityCheckFailedException: The Amazon S3 Bucket named '{self.S3_BUCKET_NAME}' was not reachable. Is it online?")
    
    def publish_file_to_s3(self):
        '''Publishes a new .txt file to Amazon S3.'''
        # Format timestamp safely (YYYY-MM-DD_HH-MM-SS).
        # e.g. 2025-02-28_00-04-21.txt
        file_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        print(f"Writing metadata to file '{file_name}' before publishing.")
        with open(file_name, "w") as f:
            f.write("This is a test file for upload.")
        print(f"Starting to publish '{file_name}' to S3 Bucket '{self.S3_BUCKET_NAME}'.")
        self.s3.upload_file(file_name, self.S3_BUCKET_NAME, file_name)
        print(f"Completed publishing '{file_name}' to S3 Bucket '{self.S3_BUCKET_NAME}'.")

    def retrieve_file_from_s3(self):
        '''Retrieves an existing .txt file from Amazon S3, then lists objects identified in bucket.'''
        print(f"Starting to retrieve file '{self.S3_BUCKET_NAME}' from Amazon S3.")
        print("Displaying items found in S3 Bucket:")
        response = self.s3.list_objects_v2(Bucket=self.S3_BUCKET_NAME)
        if "Contents" in response:
            for obj in response["Contents"]:
                print(obj["Key"])
        else:
            print(f"S3 Bucket '{self.S3_BUCKET_NAME}' is empty.")
        print(f"Completed retrieving file '{self.S3_BUCKET_NAME}' from Amazon S3.")

s3_obj = S3Manager()
s3_obj.s3_sanity_check()
s3_obj.publish_file_to_s3()
# s3_obj.retrieve_file_from_s3()