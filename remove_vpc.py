import boto3
client=boto3.client("ec2")
client.delete_vpc(
      VpcId='vpc-0a683ee82d442558d'
      )