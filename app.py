import json
from flask import Flask, request
from youtube_relevance_model import yrm


app = Flask(__name__)


@app.route('/', methods=['GET'])
def run():
    return "Hello world", 200


@app.route('/', methods=['POST'])
def hook():
    data = request.get_json()
    preds = yrm.predict(data)
    preds = json.dumps({'preds': preds.tolist()})
    return preds, 200


if __name__ == '__main__':
    app.run(debug=True)
