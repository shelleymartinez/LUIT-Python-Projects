#!/usr/bin/env python3.7

# Week 15 Project: EC2 Random Name Generator

# Create unique name generator function
import random
import string
def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

# Allow user to input number of EC2 instances they want a unique name for and identifiers
number = int(input("Enter number of EC2 instances you want to have a unique name for: "))
initials = input("Enter your initials: ")
department = input("Choose one of these departments: Marketing, Accounting, or FinOps: ")
for _ in department:
    if department == "Marketing":
        print("Marketing")
        break
    elif department == "Accounting":
        print("Accounting")
        break
    elif department == "FinOps":
        print("FinOps")
        break
    else:
        print("Error: You can not use this generator")
        exit()

# Print out the unique names of the user's EC2 instances
for _ in range(1, number + 1):
    unique_name = initials + department
    ec2_identity = unique_name + "-" + string_generator()
    print("Your EC2's unique name is: ", ec2_identity)

    