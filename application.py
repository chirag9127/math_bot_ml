import json
from flask import Flask, request
from youtube_relevance_model import yrm


application = Flask(__name__)
application.debug=True


@application.route('/', methods=['GET'])
def run():
    return "Hello world", 200


@application.route('/', methods=['POST'])
def hook():
    data = request.get_json()
    preds = yrm.predict(data)
    preds = json.dumps({'preds': preds.tolist()})
    return preds, 200


if __name__ == '__main__':
    application.run(host='0.0.0.0')
