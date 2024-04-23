# Ticker Symbol取得用
"""これは何？
ticker symbolをダウンロードして、csvに保存してdfを返す。
"""
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from PySide6 import QtWidgets

import os
import pandas as pd

from commands.make_tableview_mode import *


def search_symbol():
    # dataフォルダがなければ作成
    data_path = "data"#フォルダ名
    if not os.path.exists(data_path):#ディレクトリがなかったら
        os.mkdir(data_path)
    # NASDAQ銘柄情報取得 (Pandasデータフレーム)
    # data/ticker_symbol.csvが存在すればそれを読み込むよ
    # なければ、オンラインで読み込んでcsvを作成する。
    tickerSymbolFile = "./data/ticker_symbol.csv"
    try:
        df_ticker_symbol = pd.read_csv(tickerSymbolFile, index_col=0)
    except OSError as e:
        print(e)
        print('get Nasdaq Symbols...')
        df_ticker_symbol = get_nasdaq_symbols()
        df_ticker_symbol.to_csv('data/ticker_symbol.csv')
    else:
        pass
    return df_ticker_symbol


import requests
from pandas import json_normalize

def search_symbol_alphavantage(ticker_search_keyword):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    API_KEY='0A5DAC7F3S5UWRJZ'
    SEARCH_KEY = ticker_search_keyword
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={SEARCH_KEY}&apikey=API_KEY'

    r = requests.get(url)
    data = r.json()
    df = json_normalize(data["bestMatches"])
    return df[['1. symbol', '2. name']]



