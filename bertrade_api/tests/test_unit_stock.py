'''
Tests suid for Stock class.
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'bertade_api'))
import unittest


from models import Stock


class StockModelTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_new_stock(self):
        industries = ['Retail', 'Biotechnology', 'Beverages']
        brands_products = ['Brandio', 'Marquita', 'Baimi', 'Kaufmir']
        key_people = ['John Important IV', 'Magnus Pig']
        company_description = 'Big company'

        stock = Stock(name='Corpus corporation', yahoo_ticker='CPS',
                      bloomberg_ticker='CPS.MX', local_ticker='CPS',
                      img='http://img.ly', industries=industries,
                      brands_products=brands_products,
                      company_description=company_description,
                      listing_date='01/05/2016', key_people=key_people)

        self.assertEqual(stock.name, 'Corpus corporation')
        self.assertEqual(stock.yahoo_ticker, 'CPS')
        self.assertEqual(stock.bloomberg_ticker, 'CPS.MX')
        self.assertEqual(stock.local_ticker, 'CPS')
        self.assertEqual(stock.img, 'http://img.ly')
        self.assertEqual(stock.industries, industries)
        self.assertEqual(stock.brands_products, brands_products)
        self.assertEqual(stock.listing_date, '01/05/2016')
        self.assertEqual(stock.key_people, key_people)

    def test_find_all_stocks(self):
        stocks = Stock.find_all()
        stock_1 = stocks[0]
        self.assertEqual(stock_1.local_ticker, 'AC')
        self.assertEqual(stock_1.yahoo_ticker, '')
        self.assertEqual(stock_1.bloomberg_ticker, 'AC.MX')
        self.assertEqual(stock_1.name, 'ARCA CONTINENTAL, S.A.B. DE C.V.')
        self.assertEqual(stock_1.img, '')
        self.assertEqual(stock_1.listing_date, '13/12/2001')
        self.assertEqual(stock_1.industries, ['Consumer Staples',
                         'Consumer Products'])
        self.assertEqual(stock_1.company_description,
                         'Bottles non-alcoholic branded beverages.')
        self.assertEqual(stock_1.brands_products,
                         ['Coca-Cola', 'Ciel', 'Jugos del Valle'])
        self.assertEqual(stock_1.key_people,
                         ['Tomas Alberto Fernandez', 'Luis Arizpe'])

        stock_2 = stocks[1]
        self.assertEqual(stock_2.local_ticker, 'ALSEA')
        self.assertEqual(stock_2.yahoo_ticker, '')
        self.assertEqual(stock_2.bloomberg_ticker, 'ALSEA.MX')
        self.assertEqual(stock_2.name, 'ALSEA, S.A.B. DE C.V.')
        self.assertEqual(stock_2.img, '')
        self.assertEqual(stock_2.listing_date, '25/06/1999')
        self.assertEqual(stock_2.industries,
                         ['Consumer Discretionary', 'Restaurants'])
        self.assertEqual(stock_2.company_description,
                         'Multi-brand operator fast food and casual dining.')
        self.assertEqual(stock_2.brands_products,
                         ['Dominos Pizza', 'Starbucks', 'Burger King'])
        self.assertEqual(stock_2.key_people,
                         ['Alberto Torrado', 'Ivan Moguel'])

    def test_find_stock_by_ticker(self):
        stock = Stock.find('AC')
        self.assertEqual(stock.local_ticker, 'AC')
        self.assertEqual(stock.yahoo_ticker, '')
        self.assertEqual(stock.bloomberg_ticker, 'AC.MX')
        self.assertEqual(stock.name, 'ARCA CONTINENTAL, S.A.B. DE C.V.')
        self.assertEqual(stock.img, '')
        self.assertEqual(stock.listing_date, '13/12/2001')
        self.assertEqual(stock.industries,
                         ['Consumer Staples', 'Consumer Products'])
        self.assertEqual(stock.company_description,
                         'Bottles non-alcoholic branded beverages.')
        self.assertEqual(stock.brands_products,
                         ['Coca-Cola', 'Ciel', 'Jugos del Valle'])
        self.assertEqual(stock.key_people,
                         ['Tomas Alberto Fernandez', 'Luis Arizpe'])

    def test_single_stock_by_name(self):
        stock = Stock.find_one({'name': 'Arca Continental'})
        self.assertEqual(stock.local_ticker, 'AC')
        self.assertEqual(stock.yahoo_ticker, '')
        self.assertEqual(stock.bloomberg_ticker, 'AC.MX')
        self.assertEqual(stock.name, 'ARCA CONTINENTAL, S.A.B. DE C.V.')
        self.assertEqual(stock.img, '')
        self.assertEqual(stock.listing_date, '13/12/2001')
        self.assertEqual(stock.industries, ['Consumer Staples',
                         'Consumer Products'])
        self.assertEqual(stock.company_description,
                         'Bottles non-alcoholic branded beverages.')
        self.assertEqual(stock.brands_products,
                         ['Coca-Cola', 'Ciel', 'Jugos del Valle'])
        self.assertEqual(stock.key_people,
                         ['Tomas Alberto Fernandez', 'Luis Arizpe'])

    def test_find_allstocks_by_industry_name(self):
        stock = Stock.find({'industry': 'Consumer Products'})
        self.assertEqual(stock.yahoo_ticker, '')
        self.assertEqual(stock.bloomberg_ticker, 'AC.MX')
        self.assertEqual(stock.name, 'ARCA CONTINENTAL, S.A.B. DE C.V.')
        self.assertEqual(stock.img, '')
        self.assertEqual(stock.listing_date, '13/12/2001')
        self.assertEqual(stock.industries, ['Consumer Staples',
                         'Consumer Products'])
        self.assertEqual(stock.company_description,
                         'Bottles non-alcoholic branded beverages.')
        self.assertEqual(stock.brands_products,
                         ['Coca-Cola', 'Ciel', 'Jugos del Valle'])
        self.assertEqual(stock.key_people,
                         ['Tomas Alberto Fernandez', 'Luis Arizpe'])


if __name__ == '__main__':
    unittest.main()