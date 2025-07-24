from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    sentiment = analyzer.polarity_scores(text)
    compound = sentiment['compound']

    if compound >= 0.05:
        mood = 'positive'
    elif compound <= -0.05:
        mood = 'negative'
    else:
        mood = 'neutral'

    return jsonify({'mood': mood, 'compound': compound})

if __name__ == '__main__':
    app.run()