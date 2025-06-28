import pandas as pd
from app.config import SHORT_WINDOW, LONG_WINDOW

def moving_average_crossover(prices):
    if len(prices) < LONG_WINDOW:
        return None  # Not enough data
    short_ma = pd.Series(prices).rolling(window=SHORT_WINDOW).mean().iloc[-1]
    long_ma = pd.Series(prices).rolling(window=LONG_WINDOW).mean().iloc[-1]
    prev_short_ma = pd.Series(prices).rolling(window=SHORT_WINDOW).mean().iloc[-2]
    prev_long_ma = pd.Series(prices).rolling(window=LONG_WINDOW).mean().iloc[-2]
    if prev_short_ma < prev_long_ma and short_ma > long_ma:
        return 'buy'
    elif prev_short_ma > prev_long_ma and short_ma < long_ma:
        return 'sell'
    else:
        return None 