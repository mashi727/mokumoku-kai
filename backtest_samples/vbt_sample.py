import warnings
import yfinance as yf
import pandas as pd
import vectorbt as vbt

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def get_data(ticker:str='AAPL',from_date:str='2020-01-01',to_date:str='2022-11-30',interval:str='1d') -> pd.DataFrame:
    yf_ticker = yf.Ticker(ticker)
    return yf_ticker.history(start=from_date,end=to_date,interval=interval)


price = data = get_data(ticker='AAPL',from_date='2023-01-01',to_date='2024-3-31')['Close']


fast_ma = vbt.MA.run(price, 12)
slow_ma = vbt.MA.run(price, 24)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=10_000,freq='1D')
print(pf.stats())
pf.plot().show()
