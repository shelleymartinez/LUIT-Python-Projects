#Create Instances for Project_16.py to use for demo

import boto3
import time
ec2_resource=boto3.resource("ec2")
ec2_client=boto3.client("ec2")

# create 6 instances
ec2_resource.create_instances(
    ImageId='ami-0d9858aa3c6322f73',
    InstanceType='t2.micro',
    MaxCount=6,
    MinCount=3)
    
# Wait for instances to start up
print("Waiting for instances to startup...")
time.sleep(40) # Sleep for 40 seconds

#Print list of Instance Ids
tagged_instance = []

response=ec2_client.describe_instances()
for ids in response['Reservations']:
    for printout in ids['Instances']:
        tagged_instance.append(printout['InstanceId']) #print InstanceIds to a list
        print(tagged_instance)

# tag 3 instances for Development team
response =ec2_client.create_tags(
    Resources=[
        tagged_instance[1], tagged_instance[2], tagged_instance[3]
        ],
        Tags=[
        {
            'Key': 'Environment',
            'Value': 'dev',
        },
    ],
)
print(response)

# Stop 3 instances that are tagged: Envrionment: Dev and confirm they are running
#Find instances that are tagged and running

instances = ec2_resource.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Environment', 'Values':['dev']}])
    
# try stop tagged instances
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
    except:
        print(f'Error stopping {instance}')
