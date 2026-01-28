"""
Module to process emotion requests via the Watson NLP library
"""
import json      # Import the json library to handle parsing HTTP responses
import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyze: str) -> str:
    """
    Define a function named emotion_detector that takes a string input (text_to_analyse) and returns
    the emotion as defined the Watson NLP library as a string.
    :param text_to_analyze:
    :type text_to_analyze: str
    :return: emotion
    :rtype: str
    """
    # Set the target URL for the Watson NL Library
    url = """
    https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"""
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Send a POST request to the API with the text and headers.  Set the timeout to 10 seconds
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    # Initialise the result variable to ensure the scope is at the right level
    formatted_response = None
    # If the response status code is 200, process the response text
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
    # If the response status code is 500, set formatted text to None
    elif response.status_code == 500:
        formatted_response = None
    # Now return the formatted result
    return formatted_response
