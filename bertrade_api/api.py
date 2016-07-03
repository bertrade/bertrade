'''
'''
import argparse
from flask import Flask, jsonify, Response, request
import json

API_ROOT_URL = '/api/v1'

app = Flask(__name__)
test_mode = False


@app.route(API_ROOT_URL + '/stocks', methods=['GET'])
def get_all_stocks():
    if not test_mode:
        return Response(open('stocks.json').read(), mimetype='application/json')
    else:
        return Response(open('tests/test_stocks.json').read(), mimetype='application/json')


@app.route(API_ROOT_URL + '/stocks/<ticker>', methods=['GET'])
def get_stock_by_ticker(feature_request_id):
    return jsonify({
        'error': 'Build in progress'
    })


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
