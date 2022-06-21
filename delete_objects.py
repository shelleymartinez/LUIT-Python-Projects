import boto3

s3_resource=boto3.client("s3")

# delete single object
s3_resource.delete_object(Bucket='newbucket',
    Key='upload2.png')
    
# delete multiple objects
import os
import glob

# fing all the objects from the bucket
objects=s3_resource.list_objects(Bucket="newbucket")["Contents"]
len(objects)

# interation
for object in objects:
    response=s3_resource.delete_object(Bucket='newbucket',
        Key=object["Key"])
    print(response)

