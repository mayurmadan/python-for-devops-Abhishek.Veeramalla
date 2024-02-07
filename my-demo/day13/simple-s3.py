#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
import boto3
client = boto3.client('s3')

bucket_name = "mayur-boto-bucket"
#create the s3 bucket using boto3 with default setting
def s3_bucket_create(bucket_name):    
    response = client.create_bucket(
        #ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1',            
        },
    )
#we can change this value while execution if not provided here it will use variable's value    
s3_bucket_create(bucket_name)

#delete bucket 
def s3_bucket_delete(bucket_name):    
    response = client.delete_bucket(
        Bucket=bucket_name,
        #ExpectedBucketOwner='string'
    )
s3_bucket_delete(bucket_name)
