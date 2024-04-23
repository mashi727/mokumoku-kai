import yfinance as yf
data = yf.download("TSLA", start='2024-04-19', period='1d', interval="1m")

print(data)
