# send a message to sqs queue
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

def send_message():
    sqs_client = boto3.client("sqs", region_name="us-west-1")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl="https://us-west-2.queue.amazonaws.com/xxx/my-new-queue",
        MessageBody=json.dumps(message)
    )
    print(response)
   
   