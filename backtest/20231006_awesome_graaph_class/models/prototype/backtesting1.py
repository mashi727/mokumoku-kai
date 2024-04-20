import yfinance
import pandas as pd

from stockstats import StockDataFrame

'''
Backtesting ingests _all kinds of OHLC data_ (stocks, forex, futures, crypto, ...) as 
a pandas.DataFrame with columns 'Open', 'High', 'Low', 'Close' and (optionally) 'Volume'. 

Such data is widely obtainable (see: pandas-datareader, Quandl, findatapy). 
Besides these, your data frames can have additional columns which are accessible in your strategies in a similar manner.
DataFrame should ideally be indexed with a datetime index (convert it with pd.to_datetime()), otherwise a simple range index will do.


要するに
'Open', 'High', 'Low', 'Close' and (optionally) 'Volume'
DataFrameのインデックスは、datetimeである必要があるということ。
(convert it with pd.to_datetime())

'''


# 5年分のナスダック100指数を取ってくる例
arr = yfinance.download(
    tickers="MUFG", # ナスダック100指数
    period="max",
    interval="1m",
)

def convert_df_to_stock_df(df: pd.DataFrame) -> StockDataFrame:
    sdf = df.copy()
    sdf.rename(
        columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Adj Close": "amount",
            "Volume": "volume",
        },
        inplace=True,
    )
    sdf.index.names = ["date"]
    return StockDataFrame(sdf)

df = convert_df_to_stock_df(arr)
'''
df['rsi'] # RSI
df['macd'] # MACD
df["macds"] # MACD signal
'''


def DC(arr: pd.DataFrame, payload=20):
    count = 0

    max = []
    min = []

    df = convert_df_to_stock_df(arr).copy()
    for index, data in df.iterrows():

        if payload > count:
            # 計算できていない間は反応しないように適当に広げておく
            max.append(data["high"] + 10)
            min.append(data["low"] - 10)
            count += 1
            continue

        # 当日は含めないので-1しとく
        range = df[count - payload : count - 1]
        max.append(range["high"].max())
        min.append(range["low"].min())
        count += 1

    df["max"] = max
    df["min"] = min

    return (df["min"], df["max"])
'''
from backtesting import Strategy
class My_Strategy(Strategy):
    entry_payload_day = 20
    stop_loss_payload_day = 10

    stop_loss = 5  # percent

    day = 0

    def init(self):
        self.atr = self.I(ATR, self.data.df)

        (self.dc_min, self.dc_max) = self.I(DC, self.data.df, self.entry_payload_day)

        (self.dc_half_min, self.dc_half_max) = self.I(
            DC, self.data.df, self.stop_loss_payload_day
        )

    def next(self):
        self.day += 1

        # 計算できていない場合トレードしない
        if len(self.data.index) < self.entry_payload_day:
            return

        # 手仕舞い (半分のDCの高値または安値を下回った場合)
        if (self.dc_half_min[-1] > self.data.Low[-1] and self.position.is_long) or (
            self.data.High[-1] > self.dc_half_max[-1] and self.position.is_short
        ):
            self.position.close()
            return

        # 買い注文
        if self.data.Close[-1] > self.dc_max[-1] and not self.position.is_long:
            self.buy(sl=self.data.Close[-1] * (1 - (self.stop_loss / 100)))  # 損切り
            return

        # 売り注文
        if self.dc_min[-1] > self.data.Close[-1] and not self.position.is_short:

            self.sell(sl=self.data.Close[-1] * (1 + (self.stop_loss / 100)))  # 損切り
            return
'''

df = DC(arr)

from backtesting import Backtest

bt = Backtest(df, My_Strategy, cash=10_000, commission=.002)
stats = bt.run()
stats
