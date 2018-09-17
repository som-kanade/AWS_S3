
# python codes to perform various stuffs on AWS S3 Bucket

#create bucket
import boto3
s3 = boto3.client('s3');
response = s3.create_bucket(Bucket = 'bucketname',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)

print(response);

# Python code to upload file to S3 bucket from local system

import boto3
s3= boto3.client('s3');
response1 = s3.upload_file('test1.txt','bucketname','test1.txt');
print("file uploaded successfully")

# Python code to count number of buckets in S3  

import boto3
s3 = boto3.client('s3');
number_of_buckets = s3.list_buckets();
print(number_of_buckets);


#put object to S3 bucket

import boto3
s3 = boto3.client('s3');
response = s3.put_object(Bucket = 'BUCKETNAME',Key = 'test1.txt')
print(response);

#Get Object from S3

import boto3
s3 = boto3.client('s3');
response = s3.get_object(Bucket = 'BUCKETNAME',Key = 'test1.txt');
print(response);
