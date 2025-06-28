import time
import schedule
import os
from app.data_fetcher import fetch_price
from app.strategy import moving_average_crossover
from app.binance_trader import BinanceTrader
from app.config import SCHEDULE_MINUTES
from app.logger import log_trade

prices = []

USE_BINANCE = os.getenv('USE_BINANCE', '0') == '1'
if USE_BINANCE:
    trader = BinanceTrader()
    print("[MODE] Real trading on Binance enabled!")
else:
    from app.trader import Trader
    trader = Trader()
    print("[MODE] Paper trading mode.")

def run_bot():
    price = fetch_price()
    if price is not None:
        prices.append(price)
        print(f"Fetched price: ${price}")
        signal = moving_average_crossover(prices)
        if signal == 'buy':
            trader.buy(price)
        elif signal == 'sell':
            trader.sell(price)
        else:
            print("No trade signal.")
    else:
        print("Failed to fetch price.")

schedule.every(SCHEDULE_MINUTES).minutes.do(run_bot)

if __name__ == "__main__":
    print("Starting AI-Powered Crypto Trading Bot...")
    run_bot()  # Run once at start
    while True:
        schedule.run_pending()
        time.sleep(1) 