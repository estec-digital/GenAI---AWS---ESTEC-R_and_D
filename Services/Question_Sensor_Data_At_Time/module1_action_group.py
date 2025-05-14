import logging
from typing import Dict, Any
from http import HTTPStatus
import random
import logging
import json
from datetime import datetime, timedelta
import boto3
from boto3.dynamodb.conditions import Key, Attr
import re
from decimal import Decimal
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#config query dynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('estec-backend-alpha-RawSensorData')
factory_id = 'F_xGc676J6PH'

def query_dynamodb_for_sensor_data(factory_id_date_prefix, time_str):
    """
    Queries DynamoDB for sensor data for a specific date and time.

    Args:
        factory_id_date_prefix (str): The prefix for the FactoryId_Date key (e.g., "GA03::2025-05-13").
        time_str (str): The time to query (HH:MM:SS).

    Returns:
        list: A list of items returned from the DynamoDB query, or an empty list if no data is found.
    """
    try:
        data_query = table.query(
            KeyConditionExpression=Key('FactoryId_Date').eq(factory_id_date_prefix) & Key('Time').eq(time_str),
            ProjectionExpression='#col1, #col2, #col3, #col4, #col5, #col6, #col7, #col8, #col9, #col10',
            ExpressionAttributeNames={
                '#col1': 'Date',
                '#col2': 'Time',
                '#col3': '4G1GA01XAC01_NO_AVG',
                '#col4': '4G1GA01XAC01_O2_AVG',
                '#col5': '4G1GA02XAC01_O2_AVG',
                '#col6': '4G1GA03XAC01_O2_AVG',
                '#col7': '4G1GA04XAC01_O2_AVG',
                '#col8': '4G1KJ01JST00_T8401_AVG',
                '#col9': '4K1KP01DRV01_M2001_EI_AVG',
                '#col10': '4K1KP01KHE01_B8701_AVG'
            },
            ScanIndexForward=False,
            Limit=1
        )
        items = data_query.get('Items', [])
        if items:
            logger.info('Query successful: %s, %s', time_str, items[0])
        else:
            logger.warning(f"No data found for time {time_str}")
        return items
    except Exception as e:
        logger.error(f"Error querying DynamoDB: {e}")
        return []
# ---Start export Data function---
def detect_date_from_text(user_input):
    """
    Resolves the date based on keywords in the user input ("hôm nay", "hôm qua")
    or extracts a specific date using a regex pattern.

    Args:
        user_input (str): The input text from the user.

    Returns:
        str or None: The resolved date in 'YYYY-MM-DD' format, or None if no date is found.
    """
    today = datetime.now().date()
    if re.search(r'(?i)hôm\s*nay', user_input):
        return today.strftime('%Y-%m-%d')
    elif re.search(r'(?i)hôm\s*qua', user_input):
        yesterday = today - timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')
    else:
        # Pattern to find the date
        pattern_date = r'(?i)ngày.*?(\d{2}/\d{2}/\d{4})'
        date_match = re.search(pattern_date, user_input)
        date_str = date_match.group(1) if date_match else None
        if date_str:
            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
                return date_obj.strftime('%Y-%m-%d')
            except ValueError as e:
                logger.warning(f"Could not parse date from input: {date_str}")
                return None
        return None

def extract_date_and_time(user_input):
    """
    Extracts date and a list of times from the user input.

    Args:
        user_input (str): The input text from the user.

    Returns:
        tuple: A tuple containing the date string (YYYY-MM-DD format or None)
               and a list of time strings (HH:MM:SS format or an empty list).
    """
    resolved_date = detect_date_from_text(user_input)
    logger.info(f"Resolved date: {resolved_date}")

    # Pattern to find the time
    pattern_time = r'\b(\d{2}:\d{2}:\d{2})\b'
    times_match = re.findall(pattern_time, user_input)
    logger.info(f"All times found: {times_match}")
    
    return resolved_date, times_match
# ---End export Data function---

# ---Start compare sensor data between values---
def compare_sensor_data_by_time(sensor_data_list, time_format='%H:%M:%S', value_keys=None):
    """
    Compares sensor data based on the time of the readings.

    Args:
        sensor_data_list (list): A list of dictionaries, where each dictionary
                                 contains at least a 'Time' key (string in
                                 time_format) and one or more data value keys.
        time_format (str, optional): The format string used to parse the 'Time' key.
                                     Defaults to '%H:%M:%S'.

    Returns:
        dict: A dictionary containing comparisons between consecutive data points.
    """
    if len(sensor_data_list) < 2:
        return {}
    
    sorted_data = sorted(sensor_data_list, key=lambda x: datetime.strptime(x['Time'], time_format))
    comparisons = {}

    for i in range(len(sorted_data) - 1):
        current_data = sorted_data[i]
        next_data = sorted_data[i+1]
        time_current = current_data['Time']
        time_next = next_data['Time']

        keys_to_compare = value_keys if value_keys else [
            key for key in current_data.get('Data', {})
            if key not in ['Time', 'Date'] and isinstance(current_data.get('Data', {}).get(key), Decimal)
        ]

        for key in keys_to_compare:
            value_current = current_data.get('Data', {}).get(key)
            value_next = next_data.get('Data', {}).get(key)

            if isinstance(value_current, Decimal) and isinstance(value_next, Decimal):
                change = float(value_next - value_current)
                comparison_key = f"{key} change between {time_current} and {time_next}"
                comparisons[comparison_key] = change
    return comparisons

def process_dynamodb_data_for_comparison(dynamodb_items, time_key='Time', value_keys=None):
    """
    Processes items returned from DynamoDB into a structured list for comparison.

    Args:
        dynamodb_items (list): A list of items from DynamoDB.
        time_key (str, optional): The key representing the timestamp. Defaults to 'Time'.
        value_keys (list, optional): A list of keys to extract as sensor values.

    Returns:
        list: A list of dictionaries suitable for compare_sensor_data_by_time.
    """
    processed_data = []
    for item in dynamodb_items:
        if 'Time' in item and 'Data'in item:
            processed_item = {'Time': item['Time'], 'Data': {}}
            if value_keys:
                for key in value_keys:
                    if key in item['Data']:
                        processed_item['Data'][key] = item['Data'][key]
                    else:
                        processed_item['Data'] = item['Data']
                    processed_data.append(processed_item)
    return processed_data

def analyze_and_callback(processed_data, callback, comparison_value_keys=None):
    """
    Analyzes the processed sensor data and calls the callback function
    with the comparison results.
    """
    comparison_results = compare_sensor_data_by_time(processed_data, value_keys=comparison_value_keys)
    callback(comparison_results)

def handle_comparison_results(results):
    """
    Callback function to handle the comparison results.
    Customize this function to perform actions with the results.
    """
    logger.info("Sensor data comparison results:")
    for key, value in results.items():
        logger.info(f"- {key}: {Value}")
# ---End compare sensor data between values---

# ---Start value evaluation function is returned---
def evaluate_sensor_value_by_time(sensor_data_list, thresholds=None):
    """
    Evaluates sensor values against defined thresholds based on time.

    Args:
        sensor_data_list (list): A list of dictionaries, where each dictionary
                                 contains 'Time' and 'Data' keys.
        thresholds (dict, optional): A dictionary defining thresholds for each
                                     sensor value key within 'Data'.
                                     Example:
                                     {
                                         '4G1GA01XAC01_O2_AVG': {'high': 4.0, 'low': 3.0},
                                         '4G1GA03XAC01_O2_AVG': {'critical': 2.5}
                                     }

    Returns:
        dict: A dictionary where keys are timestamps and values are dictionaries
              containing the evaluation results for each sensor value at that time.
    """
    evaluation_results = {}
    for data_point in sensor_data_list:
        timestamp = data_point.get('Time')
        data = data_point.get('Data', {})
        if timestamp:
            evaluation_results[timestamp] = {}
            for sensor, value in data.items():
                if isinstance(value, Decimal):
                    evaluation_results[timestamp][sensor] = "Normal"
                    if thresholds and sensor in thresholds:
                        for condition, threshold_value in thresholds[sensor].items():
                            try:
                                threshold = float(threshold_value)
                                value_float = float(value)
                                if condition == '>':
                                    if value_float > threshold:
                                        evaluation_results[timestamp][sensor] = f"Above {threshold}"
                                elif condition =='<':
                                    if value_float < threshold:
                                        evaluation_results[timestamp][sensor] = f"Below {threshold}"
                                elif condition == '==':
                                    if value_float == threshold:
                                        evaluation_results[timestamp][sensor] = f"Equals {threshold}"
                                elif condition == '>=':
                                    if value_float >= threshold:
                                        evaluation_results[timestamp][sensor] = f"At or Above {threshold}"
                                elif condition == '<=':
                                    if value_float <= threshold:
                                        evaluation_results[timestamp][sensor] = f"At or Below {threshold}"
                            except ValueError:
                                logger.warning(f"Invalid threshold for {sensor}: {threshold_value}")
                else:
                    evaluation_results[timestamp][sensor] = "Invalid Value"
    return evaluation_results

def process_dynamodb_data_for_evaluation(dynamodb_items):
    """
    Processes items returned from DynamoDB into a structured list for evaluation.
    Extracts 'Time' and the 'Data' dictionary.

    Args:
        dynamodb_items (list): A list of items from DynamoDB.

    Returns:
        list: A list of dictionaries suitable for evaluate_sensor_value_by_time.
    """
    processed_data = []
    for item in dynamodb_items:
        if 'Time' in item and 'Data' in item:
            processed_data.append({'Time': item['Time'], 'Data': item['Data']})
    return processed_data

def analyze_and_callback_evaluate(processed_data, callback, evaluation_thresholds=None):
    """
    Evaluates the processed sensor data and calls the callback function
    with the evaluation results.
    """
    evaluation_results = evaluate_sensor_value_by_time(processed_data, thresholds=evaluation_thresholds)
    callback(evaluation_results)

def handle_evaluation_results(results):
    """
    Callback function to handle the sensor value evaluation results.
    Customize this function to perform actions with the results.
    """
    logger.info("Sensor value evaluation results:")
    for timestamp, evaluations in results.item():
        logger.info(f"At {timestamp}:")
        for sensor, status in evaluations.items():
            logger.info(f"- {sensor}: {status}")

# ---End value evaluation function is returned---

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handles the lambda function invocation.

    Args:
        event (dict): The event data passed to the lambda function.
        context (object): The context object passed to the lambda function.

    Returns:
        dict: A dictionary containing the query results.
    """
    try:
        user_input = event.get("inputText")
        value_keys_config = event.get("value_keys")
        thresholds_config = event.get("thresholds")
        date_str, times_to_query = extract_date_and_time(user_input)
        results = []
        logger.info(f"event data: {event}")
        if date_str and times_to_query:
            logger.info(f"User Input: {user_input}")
            dt = datetime.strptime(date_str, "%Y-%m-%d").strftime('%Y-%m-%d')
            factory_id_date_prefix = f"{factory_id}::{dt}"
            for time_str in times_to_query:
                logger.info(f"Querying for: {factory_id_date_prefix} at {time_str}")
                items = query_dynamodb_for_sensor_data(factory_id_date_prefix, time_str)
                if items:
                    logger.info('Query successful: %s, %s', time_str, items[0])
                    results.append({
                        'Time': time_str,
                        'Data': items[0]
                    })
                    logger.info(f"List result: {results}")
                else:
                    logger.warning(f"No data found for time {time_str}")
            # Compare between values of sensor
            # if len(results) >= 2:
            #     processed_data = process_dynamodb_data_for_comparison(results, value_keys_config)
            #     analyze_and_callback(processed_data, handle_comparison_results, value_keys_config)
            # else:
            #     logger.warning("Not enough data points to perform comparison")

            # Value evaluation function is returned
            # if results:
            #     processed_data_evaluate = process_dynamodb_data_for_evaluation(results)
            #     analyze_and_callback_evaluate(processed_data_evaluate, handle_evaluation_results, thresholds_config)
            # else:
            #     logger.warning("No sensor data found for the specified criteria")
        else:
            logger.warning("No date and time information found in the input")

        action_group = event.get('actionGroup')
        apiPath = event.get('apiPath')
        httpMethod =  event.get('httpMethod', 'GET')
        parameters = event.get('parameters', [])
        message_version = event.get('messageVersion',1)

        # Execute your business logic here. For more information, 
        # refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html

        # responses = ["Tôi bị ngu!"]
        responseBody =  {
            'application/json': {
                'body': results
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
