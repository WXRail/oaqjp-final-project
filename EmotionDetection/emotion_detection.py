"""
Module to process emotion requests via the Watson NLP library
"""
import json      # Import the json library to handle parsing HTTP responses
import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyze: str) -> dict:
    """
    Define a function named emotion_detector that takes a string input (text_to_analyse) and returns
    the emotion as defined the Watson NLP library as a dictionary of emotions with their values
    and the final key/pair giving the dominant emotion in the text.
    :param text_to_analyze:
    :type text_to_analyze: str
    :return: emotions and values for the text along with the dominant emotion for the text
    :rtype: dict
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
    # Initialise the result dictionary to ensure the scope is at the right level
    result = {}
    # If the response status code is 200, process the response text
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        # Pull the emotions dictionary from the emotion predictions list (index 0)
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
        # Dominant emotion and value placeholders which we will update in the for loop
        # and then reference them in the function return result.
        dominant_emotion = ""
        dominant_emotion_value = 0
        # Parse out the individual emotion keys and scores form the dictionary
        for emotion_key, emotion_value in emotions_dict.items():
            # Push these pairs into the results dictionary
            result[emotion_key] = emotion_value
            # Now check to see if this emotion is the current dominant one
            if emotion_value > dominant_emotion_value:
                # New dominant emotion found - log it for later
                dominant_emotion = emotion_key
                dominant_emotion_value = emotion_value
        # Log the dominant emotion we found into the results dictionary
        result['dominant_emotion'] = dominant_emotion
    # If the response status code is 400, set the scores to None
    elif response.status_code == 400:
        result['anger'] = None
        result['disgust'] = None
        result['fear'] = None
        result['joy'] = None
        result['sadness'] = None
        result['dominant_emotion'] = None
    # Now return the formatted result
    return result
