"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Sentiment Analyzer")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    This code receives the text from the HTML interface and
    runs sentiment analysis over it using emotion_detector()
    function. The output returned shows the label and its confidence
    score for the provided text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # First test for an invalid input which is shown by the dominant emotion as None
    if response["dominant_emotion"] is None:
        result = "Invalid text! Please try again!"
    else:
        # For a normal input, extract the emotions and scores from the response
        result = "For the given statement, the system response is "
        for key, value in response.items():
            if key == "dominant_emotion":
                result = result + f" The dominant emotion is {value}."
            else:
                result = result + f"'{key}': {value}, "
        # Now correct the grammar.
        # FInd the last comma in the string
        pattern = ","
        index = result.rfind(pattern)
        # Swap that out for a full stop
        result = result[0:index] + "." + result[index+1: len(result)]
        # Now get the previous comma
        index = result.rfind(pattern)
        # Swap that out for an 'and' and rebuild the rearmost part of the string
        result_a = result[0:index]
        result_b = result[index + 1:len(result)]
        result_b = " and" + result_b
        # Construct the result
        result = result_a + result_b
    # Return a formatted string with the emotion labels and score
    return result


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
