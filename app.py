from flask import Flask
appPort = 3000

api = Flask(__name__)

@api.route('/', methods=['GET'])
def welcome():
    return "Welcome to Azurify"

if __name__ == '__main__':
    api.run(host="0.0.0.0",port=appPort)