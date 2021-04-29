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
        ContentStr = "{\"Version\":\"2019-10-30\",\"StartAction\":\"9755647c-f2c7-47b6-8f4f-d61021708845\",\"Metadata\":{\"entryPointPosition\":{\"x\":15,\"y\":19},\"snapToGrid\":false,\"ActionMetadata\":{\"98c840c6-f533-47e2-a222-81513e4ec5f7\":{\"position\":{\"x\":1204,\"y\":448},\"useDynamic\":false},\"9755647c-f2c7-47b6-8f4f-d61021708845\":{\"position\":{\"x\":150,\"y\":24}},\"48c520b3-c013-4784-881f-b2582830f878\":{\"position\":{\"x\":1522,\"y\":456}},\"42aaf7a4-1f4d-4f77-bdfa-7fc656d4757f\":{\"position\":{\"x\":924,\"y\":336},\"useDynamic\":false},\"84793885-bbf7-46f1-a490-5b0a766f02db\":{\"position\":{\"x\":376,\"y\":19},\"conditionMetadata\":[{\"id\":\"928d0e50-89f8-4195-9acd-fa79965d0c80\",\"value\":\"1\"},{\"id\":\"36cadf36-fd3c-4ec5-bb77-840136914744\",\"value\":\"2\"}],\"useDynamic\":false},\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\":{\"position\":{\"x\":620,\"y\":25},\"dynamicMetadata\":{\"Cust_phone\":true},\"useDynamic\":false},\"9546ef89-b967-448b-95ab-733ee430b213\":{\"position\":{\"x\":1207,\"y\":634},\"useDynamic\":false},\"394d92b3-ffde-423a-a7be-733032767f9f\":{\"position\":{\"x\":1202,\"y\":287},\"useDynamic\":false},\"257e6e62-9211-4f22-b3dc-868d95e990db\":{\"position\":{\"x\":1360,\"y\":39},\"conditionMetadata\":[{\"id\":\"7eb30a01-05eb-424c-b0ec-a7317418e734\",\"value\":\"1\"},{\"id\":\"dac4df20-64b6-4e1c-8a9e-a695f291da3b\",\"value\":\"2\"}],\"useDynamic\":false},\"d111d51e-8238-46eb-80be-2fcd31b14cbd\":{\"position\":{\"x\":870,\"y\":25}},\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\":{\"position\":{\"x\":1108,\"y\":31},\"useDynamic\":false}}},\"Actions\":[{\"Identifier\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Parameters\":{\"Text\":\"Thanks for calling. Bye\"},\"Transitions\":{\"NextAction\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"9755647c-f2c7-47b6-8f4f-d61021708845\",\"Parameters\":{\"FlowLoggingBehavior\":\"Enabled\"},\"Transitions\":{\"NextAction\":\"84793885-bbf7-46f1-a490-5b0a766f02db\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"UpdateFlowLoggingBehavior\"},{\"Identifier\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Type\":\"DisconnectParticipant\",\"Parameters\":{},\"Transitions\":{}},{\"Identifier\":\"42aaf7a4-1f4d-4f77-bdfa-7fc656d4757f\",\"Parameters\":{\"Text\":\"This is lamda error\"},\"Transitions\":{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"84793885-bbf7-46f1-a490-5b0a766f02db\",\"Parameters\":{\"Text\":\"Welcome to vanity center. If you want to know the vanity numbers related to your phone number, press 1. Otherwise press 2\",\"StoreInput\":\"False\",\"InputTimeLimitSeconds\":\"10\"},\"Transitions\":{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingCondition\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"InputTimeLimitExceeded\"}],\"Conditions\":[{\"NextAction\":\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"1\"]}},{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"2\"]}}]},\"Type\":\"GetParticipantInput\"},{\"Identifier\":\"daf8d8c8-1cb9-44c7-9e44-20dd37a0724c\",\"Parameters\":{\"LambdaFunctionARN\":\"arn:aws:lambda:us-east-1:905055468705:function:vanityGenerator\",\"InvocationTimeLimitSeconds\":\"8\",\"LambdaInvocationAttributes\":{\"Cust_phone\":\"$.CustomerEndpoint.Address\"}},\"Transitions\":{\"NextAction\":\"d111d51e-8238-46eb-80be-2fcd31b14cbd\",\"Errors\":[{\"NextAction\":\"42aaf7a4-1f4d-4f77-bdfa-7fc656d4757f\",\"ErrorType\":\"NoMatchingError\"}],\"Conditions\":[]},\"Type\":\"InvokeLambdaFunction\"},{\"Identifier\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Parameters\":{\"Text\":\"Sorry. wrong input or time out. Terminating the call. Please try again later. Thanks\"},\"Transitions\":{\"NextAction\":\"48c520b3-c013-4784-881f-b2582830f878\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"394d92b3-ffde-423a-a7be-733032767f9f\",\"Parameters\":{\"Text\":\"Error due to set attributes\"},\"Transitions\":{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"},{\"Identifier\":\"257e6e62-9211-4f22-b3dc-868d95e990db\",\"Parameters\":{\"Text\":\"If you want to hear once again, please press 1. Otherwise please hang up.\",\"StoreInput\":\"False\",\"InputTimeLimitSeconds\":\"10\"},\"Transitions\":{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"Errors\":[{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingError\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"NoMatchingCondition\"},{\"NextAction\":\"9546ef89-b967-448b-95ab-733ee430b213\",\"ErrorType\":\"InputTimeLimitExceeded\"}],\"Conditions\":[{\"NextAction\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"1\"]}},{\"NextAction\":\"98c840c6-f533-47e2-a222-81513e4ec5f7\",\"Condition\":{\"Operator\":\"Equals\",\"Operands\":[\"2\"]}}]},\"Type\":\"GetParticipantInput\"},{\"Identifier\":\"d111d51e-8238-46eb-80be-2fcd31b14cbd\",\"Parameters\":{\"Attributes\":{\"varFromLambda\":\"$.External.varFromLambda\"}},\"Transitions\":{\"NextAction\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Errors\":[{\"NextAction\":\"394d92b3-ffde-423a-a7be-733032767f9f\",\"ErrorType\":\"NoMatchingError\"}],\"Conditions\":[]},\"Type\":\"UpdateContactAttributes\"},{\"Identifier\":\"e06c158b-8a8a-4a0c-8fac-4e4b4483fc3e\",\"Parameters\":{\"Text\":\"$.External.varFromLambda\"},\"Transitions\":{\"NextAction\":\"257e6e62-9211-4f22-b3dc-868d95e990db\",\"Errors\":[],\"Conditions\":[]},\"Type\":\"MessageParticipant\"}]}"

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