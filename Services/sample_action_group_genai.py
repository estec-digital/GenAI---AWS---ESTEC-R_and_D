
import logging
from typing import Dict, Any
from http import HTTPStatus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for processing Bedrock agent requests.
    
    Args:
        event (Dict[str, Any]): The Lambda event containing action details
        context (Any): The Lambda context object
    
    Returns:
        Dict[str, Any]: Response containing the action execution results
    
    Raises:
        KeyError: If required fields are missing from the event
    """
    try:
        action_group = event['actionGroup']
        apiPath = event['apiPath']
        httpMethod =  event['httpMethod']
        parameters = event.get('parameters', [])
        message_version = event.get('messageVersion',1)

        # Execute your business logic here. For more information, 
        # refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
        response_body = {
            'application/json': {
                'body': f'The API {apiPath} was called successfully with parameters: {parameters}!'
            }
        }
        action_response = {
            'actionGroup': action_group,
            'apiPath': apiPath,
            'httpMethod': httpMethod,
            'httpStatusCode': 200,
            'responseBody': responseBody
        }
        response = {
            'response': action_response,
            'messageVersion': message_version
        }

        logger.info('Response: %s', response)
        return response

    except KeyError as e:
        logger.error('Missing required field: %s', str(e))
        return {
            'statusCode': HTTPStatus.BAD_REQUEST,
            'body': f'Error: {str(e)}'
        }
    except Exception as e:
        logger.error('Unexpected error: %s', str(e))
        return {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'body': 'Internal server error'
        }
