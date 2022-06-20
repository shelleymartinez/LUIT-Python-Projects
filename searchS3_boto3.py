import boto3
resource=boto3.resource
resource=boto3.resource("s3")

# print number of buckets
bucket_list=(resource.buckets.all())
len(bucket_list)

# print name of buckets in AWS Console
for bucket in resource.buckets.all():
    print(bucket.name)
    
