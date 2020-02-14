import flask
from  flask import  jsonify
from flask_cors import CORS
from stockExchange import stateStockExchange

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/data', methods=['GET'])
def home():
    res = stateStockExchange()
    return jsonify(res)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


