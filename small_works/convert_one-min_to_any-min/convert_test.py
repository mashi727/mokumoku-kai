import pandas as pd


df_one = pd.read_csv('./20240424063830_AAPL_1min_av.csv',index_col='date', parse_dates=True)
df_five = pd.DataFrame()

def convert_time(rule):
    df_five["Open"] = df_one["Open"].resample(rule).first()
    df_five["Close"] = df_one["Close"].resample(rule).last()
    df_five["High"] = df_one["High"].resample(rule).max()
    df_five["Low"] = df_one["Low"].resample(rule).min()
    df_five["Volume"] = df_one["Volume"].resample(rule).sum()
    return df_five


time_delta = '60min'
print(convert_time(time_delta))
#print(df_one["Low"].resample('60min')
