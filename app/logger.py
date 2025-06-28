import os
import csv
from app.config import LOG_FILE

def log_trade(action, price, amount, balance, position):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as csvfile:
        fieldnames = ['action', 'price', 'amount', 'balance', 'position']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'action': action,
            'price': price,
            'amount': amount,
            'balance': balance,
            'position': position
        }) 