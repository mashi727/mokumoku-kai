'''

'''
# 4valuesからもろもろの値を算出
import datetime


ticker_symbol_Book = ['AAPL','MSFT','INTC','IBM','WFC','USB','MMM','UNP','CAT','EMR','HD','MCD','XOM','CVX','CVX','PG','KO','PEP','PM','MO','WMT','CL','MOLZ','KHC','JNJ','ABBV','AMGN','ABT','T','VZ','SO']

ticker_symbol_as_of_20231008 = ['WMT','KO','MO','PM','PG','JNJ','BMY','VZ','MCD','XOM','SPYD','AGG']


ticker_symbol = list(set(ticker_symbol_Book) | set(ticker_symbol_as_of_20231008))
#print(ticker_symbol)




t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
#print(repr(now))
# 出力例
#datetime.datetime(2021, 11, 4, 17, 37, 28, 114417, tzinfo=datetime.timezone
#(datetime.timedelta(seconds=32400), 'JST'))
#print(now)  # 2021-11-04 17:37:28.114417+09:00

# YYYYMMDDhhmmss形式に書式化
d = now.strftime('%Y%m%d%H%M%S')


def fetch_from_av(ticker_symbol, span):
    # 四本値を取ってくる。
    from alpha_vantage.techindicators import TechIndicators
    
    #symbol=ticker_symbol[0]
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key='0A5DAC7F3S5UWRJZ', output_format='pandas')
    if span == 'Daily':
        data, meta_data = ts.get_daily(symbol=ticker_symbol,outputsize='full')
    else:
        data, meta_data = ts.get_intraday(symbol=ticker_symbol,interval=span, outputsize='full')
    # 行名を変更する。
    df = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low':'Low','4. close':'Close', '5. volume':'Volume'})
    df = df.sort_index(axis=0, level=None, ascending=True)
    return df


from dataclasses import dataclass
@dataclass
class Data():
    span_av :str = '1min'
    # yahooFin [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    span_yh :str = '60m'

#print(fetch_from_av('AAPL','1min'))



import time
for ts in ticker_symbol:
    try:
        print(ts) # あああ　は文字列変数を指定していなければ"(ダブルクォート）で囲む必要がある。
        df_av = fetch_from_av(ts, '1min')
        df_av.to_csv('./data/'+d+'_'+ts+'_1min_av'+'.csv', header=True, index=True)
    except Exception as e:
        print(ts, 'Error!')
        import traceback
        with open('error.log', 'a') as f:
            traceback.print_exc( file=f)
    time.sleep(1)
    continue
