#%%

import yahoo_fin.stock_info as si
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
import numpy as np

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = [24, 8]
symbol = []
symbol.append('ZM')
print(symbol[0])
#%%
hist_data = si.get_data(symbol[0])
#print(hist_data)
chart = hist_data.plot(kind='line', y='close',color='blue')
volume = hist_data.plot(kind='line', y='volume',color='green')
#%%

#%%
income_statement = si.get_income_statement(symbol[0], yearly = False)
print(income_statement)
#%%
income_statement_for_graph = si.get_income_statement(symbol, yearly = False).transpose()
income_statement_for_graph.plot(kind='line', y='totalRevenue',color='blue')
#%%
from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader

pd.set_option('display.max_columns', None)

income_statement = si.get_income_statement("aapl", yearly=False)
print(income_statement)

# %%
