'''
'''
import argparse
from flask import Flask, jsonify, request
import json

from models import Stock

API_ROOT_URL = '/api/v1'

app = Flask(__name__)
test_mode = False

if not test_mode:
    json_path = 'stocks.json'
else:
    json_path = 'tests/test_stocks.json'


@app.route(API_ROOT_URL + '/stocks', methods=['GET'])
def get_all_stocks():
    stocks = Stock.find_all(test_mode=test_mode)
    return jsonify(stocks=stocks['stocks'])


@app.route(API_ROOT_URL + '/stocks/<local_ticker>', methods=['GET'])
def get_stock_by_ticker(local_ticker):
    stock = Stock.find({'local_ticker': local_ticker}, test_mode=test_mode)
    print stock
    return jsonify(stock)


@app.route(API_ROOT_URL + '/build-strategy', methods=['POST'])
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
        'message': 'Endpoint does not exist'
    }), 404

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='dev')
    parser.add_argument('-p', '--public', default='false')
    args = vars(parser.parse_args())
    if args['mode'] == 'test':
        test_mode = True
    if args['public'] == 'true':
        app.run('0.0.0.0')
    else:
        app.run(debug=True)
