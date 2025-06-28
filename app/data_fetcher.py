import requests
from app.config import SYMBOL, CURRENCY

def fetch_price():
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={SYMBOL}&vs_currencies={CURRENCY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[SYMBOL][CURRENCY]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None 