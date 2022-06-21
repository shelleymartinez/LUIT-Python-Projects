# How to list objects from bucket
import boto3
s3_resources=boto3.client("s3")

objects=s3_resources.list_objects(Bucket="newbucket")["Contents"]

# Find number of file
len(objects)
    
if len(objects)>0:
    print("objects exits")
    
# Find name of files
    
for object in objects:
    print(object["Key"])