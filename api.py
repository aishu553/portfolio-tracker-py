import requests

API_KEY = 'GV5D36M2J6NDPKLP' 
BASE_URL = 'https://www.alphavantage.co/query'

def get_current_price(symbol):
    try:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        price = float(data["Global Quote"]["05. price"])
        return price
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None
