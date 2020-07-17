# Sends binary data from AWS S3 to API Gateway via AWS Lambda function through lambda proxy integration

import json
import base64
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")    
    
    # for lambda proxy integration 
    bucket_name = event['pathParameters']['bucket']
    file_name = event['queryStringParameters']['file']
    
    file_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = file_object["Body"].read()
    
    print(bucket_name, file_name)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf"
        },
        "body" : base64.b64encode(file_content),
        "isBase64Encoded": True
    }
    
    # In case one wants to send json as response
    
    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Content-Type": "application/json"
    #     },
    #     "body" : json.dumps("Json response"),
    #     "isBase64Encoded": False
    # }