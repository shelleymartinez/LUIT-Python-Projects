#!/usr/bin/env python3.7
import boto3

def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("Learning python is fun.")

if __name__=="__main__":
    main()
