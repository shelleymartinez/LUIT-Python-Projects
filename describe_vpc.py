import boto3

client=boto3.client("ec2")

# how to describe all available vpc's in your account
x=client.describe_vpcs()
number_of_vpcs=x["VPCs"]#lists VPCs by dictionary
len(number_of_vpcs)#number of vpcs

for vpc in number_of_vpcs:#prints list of VPCIDs
    print(vpc["VPCId"])
    
# how to describe a vpc using vpc IDs
x=client.describe_vpcs(VpcIds=["input VPC IDs"])

# how to describe vpc using filters
x=client.describe_vpcs
x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  'vpc-06f85a6d',
                  'vpc-0726e99e7bc27be14'
                  
              ]
          },
      ])
