def get_price(currency):
    return currency['quote']['USD']['price']


def get_symbol(currency):
    return currency['symbol']


def get_name(currency):
    return currency['name']


def get_1h_percent_change(currency):
    return currency['quote']['USD']['percent_change_1h']


def get_24h_percent_change(currency):
    return currency['quote']['USD']['percent_change_1h']


def get_main_info(currency):
    return {"name": get_name(currency),
            "symbol": get_symbol(currency),
            "price": get_price(currency)}
