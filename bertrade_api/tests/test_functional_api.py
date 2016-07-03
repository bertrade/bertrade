'''
Tests suite for API endpoints.
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
        self.api.test_mode = True

    def _assert_first_stock(self, assert_obj):
        expected_stock = {
            'local_ticker': 'ALSEA',
            'yahoo_ticker': '',
            'bloomberg_ticker': 'ALSEA.MX',
            'name': 'ALSEA, S.A.B. DE C.V.',
            'img': '',
            'listing_date': '25\/06\/1999',
            'industries': ['Consumer Discretionary', 'Restaurants'],
            'company_description': 'Multi-brand operator fast food and casual dining.',
            'brands_products': ['Dominos Pizza', 'Starbucks', 'Burger King'],
            'key_people': ['Alberto Torrado', 'Ivan Moguel']
        }
        self.assertEqual(expected_stock, assert_obj)

    def test_list_stocks(self):
        response = self.api.get(API_ROOT_URL + '/stocks')
        response_test = json.loads(response.data)
        expected_stocks = {
            'stock_exchange': 'bmv',
            'stocks': [{
                'local_ticker': 'AC',
                'yahoo_ticker': '',
                'bloomberg_ticker': 'AC.MX',
                'name': 'ARCA CONTINENTAL, S.A.B. DE C.V.',
                'img': '',
                'listing_date': '13\/12\/2001',
                'industries': ['Consumer Staples', 'Consumer Products'],
                'company_description': 'Bottles non-alcoholic branded beverages.',
                'brands_products': ['Coca-Cola', 'Ciel', 'Jugos del Valle'],
                'key_people': ['Tomas Alberto Fernandez', 'Luis Arizpe']
            }, {
                'local_ticker': 'ALSEA',
                'yahoo_ticker': '',
                'bloomberg_ticker': 'ALSEA.MX',
                'name': 'ALSEA, S.A.B. DE C.V.',
                'img': '',
                'listing_date': '25\/06\/1999',
                'industries': ['Consumer Discretionary', 'Restaurants'],
                'company_description': 'Multi-brand operator fast food and casual dining.',
                'brands_products': ['Dominos Pizza', 'Starbucks', 'Burger King'],
                'key_people': ['Alberto Torrado', 'Ivan Moguel']
            }]
        }
        self.assertEqual(expected_stocks, response_test)

    def test_stock_by_ticker(self):
        response = self.api.get(API_ROOT_URL + '/stocks/ALSEA')
        response_test = json.loads(response.data)
        self._assert_first_stock(response_test)

    def test_stock_by_name(self):
        response = self.api.get(API_ROOT_URL + '/stocks?name=ALSEA')
        response_test = json.loads(response.data)
        self._assert_first_stock(response_test)

    def test_stock_by_industry_name(self):
        response = self.api.get(API_ROOT_URL + '/stocks?industry=Restaurants')
        response_test = json.loads(response.data)
        self._assert_first_stock(response_test)

    def test_compare_stocks(self):
        response = self.api.get(API_ROOT_URL + '/compare-stocks?a=AC&b=ALSEA')
        self.fail('Test not finished!')

    def test_build_strategy(self):
        response = self.api.post(API_ROOT_URL + '/build-strategy')
        self.fail('Test not finished!')

if __name__ == '__main__':
    unittest.main()
