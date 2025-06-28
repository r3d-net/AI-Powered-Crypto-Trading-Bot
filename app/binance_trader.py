import os
from binance.client import Client
from app.config import TRADE_AMOUNT, SYMBOL, CURRENCY

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

# Map CoinGecko symbol to Binance symbol (e.g., 'bitcoin' -> 'BTCUSDT')
BINANCE_SYMBOL = 'BTCUSDT'

class BinanceTrader:
    def __init__(self):
        self.client = client

    def buy(self, price):
        # Market buy order for TRADE_AMOUNT USD worth of BTC
        quantity = round(TRADE_AMOUNT / price, 6)
        try:
            order = self.client.create_order(
                symbol=BINANCE_SYMBOL,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            print(f"[BINANCE] Bought {quantity} BTC at market price.")
            return order
        except Exception as e:
            print(f"[BINANCE] Buy order failed: {e}")
            return None

    def sell(self, price):
        # Market sell order for TRADE_AMOUNT USD worth of BTC
        quantity = round(TRADE_AMOUNT / price, 6)
        try:
            order = self.client.create_order(
                symbol=BINANCE_SYMBOL,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            print(f"[BINANCE] Sold {quantity} BTC at market price.")
            return order
        except Exception as e:
            print(f"[BINANCE] Sell order failed: {e}")
            return None 