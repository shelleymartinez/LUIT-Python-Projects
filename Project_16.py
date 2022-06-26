# A python script that you can run that will stop 3 instances

import boto3
ec2_resource=boto3.resource("ec2")
ec2_client=boto3.client("ec2")
    
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
for Instance_State in tagged_instances:
    if Instance_State == "running":
        response = ec2_client.stop_instances(InstanceIds=tagged_instances)
    else:
        print("nothing to stop")