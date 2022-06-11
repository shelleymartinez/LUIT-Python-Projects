#!/usr/bin/env python3.7
# create a variable to hold a list of aws services
aws_services = []

# add services to the list
aws_services.append('Cloud9')
aws_services.append('DynamoDB')
aws_services.append('EC2')
aws_services.append('GuardDuty')
aws_services.append('IAM')
aws_services.append('Kinesis')

# print the list and the length of the list

length = len(aws_services)
print("This is a list of AWS services:", aws_services, "and the length of the list is:", length)

# remove two services from the list and print the new list

del aws_services[3]
del aws_services[4]
new_list = list(aws_services)

print("I have removed two services and this is the new list:", new_list)

# print length of the list
new_length = len(new_list)
print("This is the length of the new list:", new_length)
