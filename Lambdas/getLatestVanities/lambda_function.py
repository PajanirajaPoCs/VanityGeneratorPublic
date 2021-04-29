import json
import boto3

dynamodb = boto3.resource("dynamodb")

def fetchData():
    vanityHistory = dynamodb.Table("callerVanity")
    response = vanityHistory.scan()
    return response["Items"]
    
def lambda_handler(event, context):
    # TODO implement
    result = fetchData()
    return {
        'statusCode': 200,
        "headers":{
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        },
        'body': result
    }
