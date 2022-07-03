# lambda function to send sqs
import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-west-1'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sqs_client = boto3.client("sqs", region_name=AWS_REGION)
queue_url = 'https://sqs.us-west-1.amazonaws.com/789034859404/standard_sqs'

def lambda_handler(event, context):
    
    sqs_client = boto3.client("sqs", region_name="us-west-1")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-west-1.amazonaws.com/789034859404/standard_sqs",
        MessageBody=json.dumps(message)
    )
    print(response)
   