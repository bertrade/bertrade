'''
Tests API endpoints
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'bertade_api'))
import unittest

from flask import json

from api import app

API_ROOT_URL = '/api/v1'

class BertradeApiTest(unittest.TestCase):

    def setUp(self):
        self.api = app.test_client()

    def tearDown(self):
        pass

    def test_list_stocks(self):
        response = self.api.get(API_ROOT_URL + '/stocks')
        response_test = json.loads(response.data)
        self.assertEqual({}, response_test)
        self.fail('Test not finished!')

    def test_stock_by_ticker(self):
        response = self.api.get(API_ROOT_URL + '/stocks/CREAL')
        response_test = json.loads(response.data)
        self.assertEqual({}, response_test)
        self.fail('Test not finished!')

    def test_stock_by_name(self):
        response = self.api.get(API_ROOT_URL + '/stocks?name=FUNO')
        response_test = json.loads(response.data)
        self.assertEqual({}, response_test)
        self.fail('Test not finished!')

    def test_compare_stocks(self):
        response = self.api.get(API_ROOT_URL + '/compare-stocks?a=CREAL&b=FSHOP')
        response_test = json.loads(response.data)
        self.assertEqual({}, response_test)
        self.fail('Test not finished!')

    def test_build_strategy(self):
        response = self.api.post(API_ROOT_URL + '/build-strategy')
        response_test = json.loads(response.data)
        self.assertEqual({}, response_test)
        self.fail('Test not finished!')

if __name__ == '__main__':
    unittest.main()
