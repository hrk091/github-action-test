import json
import requests

def lambda_handler(event, context):
    print(requests.__version__)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello world from GitHub Actions!!')
    }
