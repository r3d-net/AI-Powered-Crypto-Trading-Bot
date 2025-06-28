import os
from app.config import LOG_FILE, TRADE_AMOUNT
from app.logger import log_trade

class Trader:
    def __init__(self):
        self.balance = 10000  # Starting USD balance
        self.position = 0     # Amount of BTC held
        self.last_price = None

    def buy(self, price):
        amount = TRADE_AMOUNT / price
        if self.balance >= TRADE_AMOUNT:
            self.balance -= TRADE_AMOUNT
            self.position += amount
            log_trade('buy', price, amount, self.balance, self.position)
            print(f"Bought {amount:.6f} BTC at ${price}")

    def sell(self, price):
        amount = TRADE_AMOUNT / price
        if self.position >= amount:
            self.balance += TRADE_AMOUNT
            self.position -= amount
            log_trade('sell', price, amount, self.balance, self.position)
            print(f"Sold {amount:.6f} BTC at ${price}") 