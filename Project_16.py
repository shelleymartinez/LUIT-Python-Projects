# A python script that you can run that will stop 3 instances

import boto3
ec2_resource=boto3.resource("ec2")
ec2_client=boto3.client("ec2")

# create 6 instances
ec2_resource.create_instances(
    ImageId='ami-0d9858aa3c6322f73',
    InstanceType='t2.micro',
    MaxCount=5,
    MinCount=3)
    
# list instance ids
response=ec2_client.describe_instances()
instances=response['Reservations']
instance_ids = []

for instance in instances:
    instance_ids.append(instance['Instances'] [0] ['InstanceId'])

# tag 3 instances for Development team
tagged_instances = (instance_ids[1:4])
tag_creation = ec2_client.create_tags(
    Resources =
        tagged_instances,
    Tags = [
        {
            'Key':'Environment',
            'Value': 'Dev'
        }
    ]
)

# stop instances
response = ec2_client.stop_instances(InstanceIds=tagged_instances)