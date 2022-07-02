# Stop 3 instances that are tagged: Envrionment: Dev and confirm they are running
import boto3
ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

#Find instances that are tagged and running
instances = ec2.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name': 'tag:Environment', 'Values':['dev']}])
    
# try stop tagged instances
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
    except:
        print(f'Error stopping {instance}')