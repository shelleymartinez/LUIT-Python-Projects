# used to list instance Ids and tag instances for Create_instances.py
import boto3
ec2_client=boto3.client("ec2")

#Print list of Instance Ids
import boto3
ec2_client = boto3.client('ec2')
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

