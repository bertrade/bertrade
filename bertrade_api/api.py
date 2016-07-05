'''
'''
import argparse
from flask import Flask, jsonify, request
import json

from models import Stock

API_ROOT_URL = '/api/v1'

app = Flask(__name__)

if not app.testing:
    json_path = 'stocks.json'
else:
    json_path = 'tests/test_stocks.json'


@app.route(API_ROOT_URL + '/stocks/', methods=['GET'])
def get_all_stocks(name=None):
    search_name = request.args.get('name')
    if search_name:
        stock = Stock.find_one({'name': search_name}, test_mode=app.testing)
        return jsonify(stock=stock)
    industry = request.args.get('industry')
    if industry:
        stocks = Stock.find({'industry': industry}, test_mode=app.testing)
        return jsonify(stocks=stocks)
    # Get all stocks
    stocks = Stock.find_all(test_mode=app.testing)
    return jsonify(stocks=stocks['stocks'])


@app.route(API_ROOT_URL + '/stocks/<local_ticker>', methods=['GET'])
def get_stock_by_ticker(local_ticker):
    stock = Stock.find_one({'local_ticker': local_ticker}, test_mode=app.testing)
    return jsonify(stock=stock)


@app.route(API_ROOT_URL + '/build-strategy/', methods=['POST'])
def build_strategy():
    data = request.data
    data_dict = json.loads(data)
    return jsonify({
        'error': 'Build in progress'
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint does not exist',
        'path': request.path
    }), 404

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='dev')
    parser.add_argument('-p', '--public', default='false')
    args = vars(parser.parse_args())
    if args['mode'] == 'test':
        app.testing = True
    if args['public'] == 'true':
        app.run('0.0.0.0')
    else:
        app.run(debug=True)
