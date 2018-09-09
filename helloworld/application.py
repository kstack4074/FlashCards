#!flask/bin/python
import json
from flask import Flask, Response

from Dynamo.dynamo import DynamoTable
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/<topic>', methods=['GET'])
def getCardWithTopic(topic):
    flashCardTable = DynamoTable('Cards')
    return Response(json.dumps({'Topic': flashCardTable.getEverything()}), mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)
