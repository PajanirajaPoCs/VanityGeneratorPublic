import json
import cfnresponse
import boto3
import os

client = boto3.client('connect')

region = os.environ['Region']
accNo = os.environ['AccountNumber']
instanceId = os.environ['instanceId']
contactFlowName = os.environ['contactFlowName']

def lambda_handler(event, context):
    try:
        ContentStr = "{\"Version\":\"2019-10-30\",\"StartAction\":\"9755647c-f2c7-47b6-8f4f-d61021708845\",\"Metadata\":{\"entryPointPosition\":{\"x\":15,\"y\":15},\"snapToGrid\":false,\"ActionMetadata\":{\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\":{\"position\":{\"x\":1331,\"y\":34},\"useDynamic\":false},\"9755647c-f2c7-47b6-8f4f-d61021708845\":{\"position\":{\"x\":150,\"y\":20}},\"2f8163a2-f560-45a8-a0b3-570a2cecbf63\":{\"position\":{\"x\":633,\"y\":16},\"useDynamic\":false},\"98c840c6-f533-47e2-a222-81513e4ec5f7\":{\"position\":{\"x\":1204,\"y\":444},\"useDynamic\":false},\"48c520b3-c013-4784-881f-b2582830f878\":{\"position\":{\"x\":1522,\"y\":452}},\"84793885-bbf7-46f1-a490-5b0a766f02db\":{\"position\":{\"x\":376,\"y\":15},\"conditionMetadata\":[{\"id\":\"855ceaac-58b6-4f43-a3db-09edc85b4c95\",\"value\":\"1\"},{\"id\":\"40011ace-b49f-4217-85ae-641b2b49d8f4\",\"value\":\"2\"}],\"useDynamic\":false},\"257e6e62-9211-4f22-b3dc-868d95e990db\":{\"position\":{\"x\":1563,\"y\":35},\"conditionMetadata\":[{\"id\":\"6af2de6b-035a-4cb9-bc1f-0bb4131c884e\",\"value\":\"1\"}],\"useDynamic\":false},\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\":{\"position\":{\"x\":875,\"y\":26},\"dynamicMetadata\":{\"Cust_phone\":true},\"useDynamic\":false},\"d111d51e-8238-46eb-80be-2fcd31b14cbd\":{\"position\":{\"x\":1101,\"y\":28}},\"9546ef89-b967-448b-95ab-733ee430b213\":{\"position\":{\"x\":1207,\"y\":630},\"useDynamic\":false}}},\"Actions\":[{\"Identifier\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Parameters\":{\"Text\":\"$.External.varFromLambda\"},\"Transitions\":{\"NextAction\":\"257e6e62-9211-4f22-b3dc-868d95e990db\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"9755647c-f2c7-47b6-8f4f-d61021708845\",\"Parameters\":{\"FlowLoggingBehavior\":\"Enabled\"},\"Transitions\":{\"NextAction\":\"84793885-bbf7-46f1-a490-5b0a766f02db\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"UpdateFlowLoggingBehavior\"},{\"Identifier\":\"2f8163a2-f560-45a8-a0b3-570a2cecbf63\",\"Parameters\":{\"Text\":\"Note:  last 7 digits of your phone number will be considered for vanity generation. Kindly hold few seconds to check the possibilities of vanities.\"},\"Transitions\":{\"NextAction\":\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Parameters\":{\"Text\":\"Thanks for calling. Bye\"},\"Transitions\":{\"NextAction\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Type\":\"DisconnectParticipant\",\"Parameters\":{},\"Transitions\":{}},{\"Identifier\":\"84793885-bbf7-46f1-a490-5b0a766f02db\",\"Parameters\":{\"Text\":\"Welcome to vanity center. If you want to know the vanity numbers related to your phone number, press 1. Otherwise press 2\",\"StoreInput\":\"False\",\"InputTimeLimitSeconds\":\"10\"},\"Transitions\":{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"},{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"ErrorType\":\"NoMatchingCondition\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"InputTimeLimitExceeded\"}],\"Conditions\":[{\"NextAction\":\"2f8163a2-f560-45a8-a0b3-570a2cecbf63\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"1\"]}},{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"2\"]}}]},\"Type\":\"GetParticipantInput\"},{\"Identifier\":\"257e6e62-9211-4f22-b3dc-868d95e990db\",\"Parameters\":{\"Text\":\"If you want to hear your vanities once again, please press 1. Otherwise please hang up.\",\"StoreInput\":\"False\",\"InputTimeLimitSeconds\":\"10\"},\"Transitions\":{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"},{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"ErrorType\":\"NoMatchingCondition\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"InputTimeLimitExceeded\"}],\"Conditions\":[{\"NextAction\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"1\"]}}]},\"Type\":\"GetParticipantInput\"},{\"Identifier\":\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\",\"Parameters\":{\"LambdaFunctionARN\":\"arn:aws:lambda:us-east-1:905055468705:function:vanityGenerator\",\"InvocationTimeLimitSeconds\":\"8\",\"LambdaInvocationAttributes\":{\"Cust_phone\":\"$.CustomerEndpoint.Address\"}},\"Transitions\":{\"NextAction\":\"d111d51e-8238-46eb-80be-2fcd31b14cbd\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"}],\"Conditions\":[]},\"Type\":\"InvokeLambdaFunction\"},{\"Identifier\":\"d111d51e-8238-46eb-80be-2fcd31b14cbd\",\"Parameters\":{\"Attributes\":{\"varFromLambda\":\"$.External.varFromLambda\"}},\"Transitions\":{\"NextAction\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"}],\"Conditions\":[]},\"Type\":\"UpdateContactAttributes\"},{\"Identifier\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Parameters\":{\"Text\":\"Sorry. Wrong input or time out. Please try again later. Thanks\"},\"Transitions\":{\"NextAction\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"}]}"

        dataList = json.loads(ContentStr)
        dictt = {}

#-------Replacing Lambda ARN and Accociating with Connect Instance--------------        
        for data in dataList['Actions']:
            dictt = data['Parameters']
            if 'LambdaFunctionARN' in dictt.keys():
                reg = data['Parameters']['LambdaFunctionARN'].split(':')[3]
                acc = data['Parameters']['LambdaFunctionARN'].split(':')[4]
                data['Parameters']['LambdaFunctionARN'] = data['Parameters']['LambdaFunctionARN'].replace(reg,region)
                data['Parameters']['LambdaFunctionARN'] = data['Parameters']['LambdaFunctionARN'].replace(acc,accNo)
                response = client.associate_lambda_function(
                    InstanceId = instanceId,
                    FunctionArn = data['Parameters']['LambdaFunctionARN']
                )

#-------Creating ContactFlow---------------------------------------------------- 
        ContentStr = json.dumps(dataList)
        response = client.create_contact_flow(
            InstanceId = instanceId,
            Name = contactFlowName,
            Type = 'CONTACT_FLOW',
            Content = ContentStr
        )

#-------Sending Success Response to Custom Resoruce-----------------------------        
        responseValue = 'Success'
        responseData = {}
        responseData['Message'] = responseValue
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID") 
    
    except:
        responseValue = 'Failed'
        responseData = {}
        responseData['Message'] = responseValue
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")  