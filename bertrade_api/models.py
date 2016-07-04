'''
Models.
'''
import json

from fuzzywuzzy import fuzz

MIN_FUZZ_RATIO = 98


class Stock():
    def __init__(self, **kwargs):
        name = kwargs.get('name')
        yahoo_ticker = kwargs.get('yahoo_ticker')
        bloomberg_ticker = kwargs.get('bloomberg_ticker')
        local_ticker = kwargs.get('local_ticker')
        listing_date = kwargs.get('listing_date', [])

        # Optional args
        test_mode = kwargs.get('test_mode', False)
        img = kwargs.get('img')
        industries = kwargs.get('industries', [])
        brands_products = kwargs.get('brands_products', [])
        company_description = kwargs.get('company_description', [])
        key_people = kwargs.get('key_people', [])

        self.name = name
        self.yahoo_ticker = yahoo_ticker
        self.bloomberg_ticker = bloomberg_ticker
        self.local_ticker = local_ticker
        self.listing_date = listing_date
        self.img = img
        self.industries = industries
        self.brands_products = brands_products
        self.key_people = key_people
        self.company_description = company_description
        self.test_mode = test_mode

    @staticmethod
    def _compare_strings(a, b):
        if fuzz.partial_ratio(a, b) >= MIN_FUZZ_RATIO:
            return True
        if fuzz.token_set_ratio(a, b) == 100:
            return True
        return False

    @staticmethod
    def find_one(search_dict, test_mode=False, as_dict=True):
        if not test_mode:
            json_path = 'stocks.json'
        else:
            json_path = 'tests/test_stocks.json'
        stocks = json.load(open(json_path))

        if search_dict.get('local_ticker'):
            for stock in stocks['stocks']:
                if stock['local_ticker'] == search_dict['local_ticker']:
                    return stock
        if search_dict.get('name'):
            for stock in stocks['stocks']:
                if Stock._compare_strings(stock['name'], search_dict['name']):
                    return stock

        return {'error': 'Stock not found'}

    @staticmethod
    def find(search_dict, test_mode=False, as_dict=True):
        if not test_mode:
            json_path = 'stocks.json'
        else:
            json_path = 'tests/test_stocks.json'
        stocks = json.load(open(json_path))

        if search_dict.get('industry'):
            matching_stocks = []
            for stock in stocks['stocks']:
                for industry in stock['industries']:
                    if Stock._compare_strings(industry, search_dict['industry']):
                        matching_stocks.append(stock)
                        break
            return matching_stocks

    @staticmethod
    def find_all(test_mode=False, as_dict=True):
        if not test_mode:
            json_path = 'stocks.json'
        else:
            json_path = 'tests/test_stocks.json'
        stocks = json.load(open(json_path))
        return stocks
