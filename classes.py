import requests


class Bot:

    def __init__(self):

        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        self. orders = []

        self.params = {
            'start': '1',
            'limit': '100',
            'convert': 'USD',
            'sort': 'market_cap',
            'sort_dir': 'desc',
            'volume_24h_min': '0'
        }

        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'ADD_YOUR_KEY_HERE'
        }

    # [ITA] Metodo principale per il recupero di dati da CoinMarketCap
    # [ITA] Per maggiori informazioni visita https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency

    # [ENG] Main method for recovering data from CoinMarketCap
    # [ENG] For more information visit https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency
    def fetch_currencies_data(self, sort="market_cap", limit=100, sort_dir="desc", volume_24h_min='0'):

        self.params["limit"] = str(limit)
        self.params["sort"] = sort
        self.params["sort_dir"] = sort_dir
        self.params["volume_24h_min"] = str(volume_24h_min)

        r = requests.get(url=self.url, headers=self.headers, params=self.params).json()

        return r['data']
