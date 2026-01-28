"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
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

    # Extract the label and score from the response
    # label = response['label']
    # score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if response is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return f"{response}"


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
