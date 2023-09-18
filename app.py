from flask import Flask, request, jsonify
import json
appPort = 3000

api = Flask(__name__)

@api.route('/', methods=['GET'])
def welcome():
    return "Welcome to Azurify"

@api.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{'pubsubname': 'pubsub', 'topic': 'A', 'route': 'A'}]
    return jsonify(subscriptions)

@api.route('/A', methods=['POST'])
def a_subscriber():
    print(f'A: {request.json}', flush=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    api.run(host="0.0.0.0",port=appPort)