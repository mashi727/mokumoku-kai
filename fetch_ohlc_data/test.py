import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://alphavantageapi.co/timeseries/analytics?SYMBOLS=AAPL,MSFT,IBM&RANGE=2023-07-01&RANGE=2023-08-31&INTERVAL=DAILY&OHLC=close&CALCULATIONS=MEAN,STDDEV,CORRELATION&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
