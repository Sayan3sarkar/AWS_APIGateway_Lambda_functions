# Sends binary data from AWS S3 to API Gateway via AWS Lambda function through legacy methods

import json
import base64
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    
    print(event) # Helps to obtain path for bucket_name and file_name by monitoring in cloudwatch logs
    
    # for legacy method
    bucket_name = event['params']['path']['bucket'] # Obtained as request path parameter
    file_name = event['params']['querystring']['file'] # Obtained as query parameter
    file_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = file_object["Body"].read()
    
    # file_content = b"hello"
    # print(type(file_content))
    
    # for lambda proxy integration 
    # bucket_name = event['pathParameters']['bucket']
    # file_name = event['queryStringParameters']['file']
    
    print(bucket_name, file_name)
    return base64.b64encode(file_content)
