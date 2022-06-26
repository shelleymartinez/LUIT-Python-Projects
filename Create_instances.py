#Create Instances for Project_16.py to use for demo

import boto3
ec2_resource=boto3.resource("ec2")
ec2_client=boto3.client("ec2")

# create 3 instances
ec2_resource.create_instances(
    ImageId='ami-0d9858aa3c6322f73',
    InstanceType='t2.micro',
    MaxCount=6,
    MinCount=3)