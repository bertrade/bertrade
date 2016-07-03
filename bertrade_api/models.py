'''
Models.
'''


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
    def find(search_dict, test_mode=False):
        return None

    @staticmethod
    def find_one(search_dict, test_mode=False):
        return None

    @staticmethod
    def find_all(test_mode=False):
        return []
