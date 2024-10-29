import json
import boto3

client_bedrock_agent = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    
    print('The event is: ', event)
    
    user_prompt = event['prompt']
    print('The user prompt is: ',user_prompt)
    
    knowledge_base_response = client_bedrock_agent.retrieve_and_generate(
        input = {
            'text': user_prompt
        },
        retrieveAndGenerateConfiguration = {
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': 'HHVRDAHJLZ',
                'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2:1'
                }
            }
        )
        
    print('knowledge_base_response is: ', knowledge_base_response)
    print('the final response is: ', knowledge_base_response['output']['text'])
    print('citations: ', knowledge_base_response['citations'][0]['generatedResponsePart']['textResponsePart'])
    
    return {
        'statusCode': 200,
        'body': knowledge_base_response['output']['text']
    }
