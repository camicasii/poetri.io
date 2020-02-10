import flask
from  flask import  jsonify, request
from  myZone.stockExchange import stateStockExchange

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    res = stateStockExchange()
    return jsonify(res)


app.run()


