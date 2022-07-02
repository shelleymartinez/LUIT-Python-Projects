import json
import os
import datetime

import boto3

QueueName = os.environ['QueueName']
Max_queue_messages = os.environ['Max_queue_messages']
DynamoDB_Table = os.environ['DynamoDB_Table']

sqs = boto3.resource('sqs')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    queue = sqs.get_queue_by_name(QueueName=QueueName) # Receive messages from SQS
    
    print("Approximate number of messages: ",
        queue.attributes.get('ApproximateNumberofMessages'))
        
    for message in queue.receive.messages(
        MaxNumberofMessages=int(Max_queue_messages)):
            
        print(message)
            
            
        table = dynamodb.Table(DynamoDB_Table) # Write message to DynamoDB
            
        response = table.put_item(
            Item={
            'MessageId': message['messageId'],
            'Body': message['body'],
            'Timestamp': datetime.time().isoformat()
            }
        )
        print("Wrote message to DynamoDB:", json.dumps(response))
        
        # Delete message
        message.delete()
        print("Deleted message:", message.messageId)
