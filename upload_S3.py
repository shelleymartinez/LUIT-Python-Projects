import boto3

# How to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="upload.png",
    Bucket="newbucket",
    Key="uploadtxt.png")
    
# How to upload multile files
import os
import glob

cwd=os.getcwd() #find file path
cwd=cwd+"/upload/" #source directory
files=glob.glob(cwd+"*.png") #input file type i.e. ".png" or ".txt" ect.

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="newbucket",
    Key=file.split("/")[-1])
    
