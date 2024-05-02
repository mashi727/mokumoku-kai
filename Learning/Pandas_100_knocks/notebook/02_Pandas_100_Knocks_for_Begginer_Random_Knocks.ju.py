# %% [markdown]
"""
# 【ランダムノック】初学者向けPandas100本ノックver1.0.7
##### 1～89までの問題をランダムに表示
##### Shift + Enter で各セルのコードが実行されます
・print(ans[ 問題番号 ]) で回答コード例を表示  
・Python3エンジニア認定データ分析試験にも沿った問題内容   
・Pandasの各メソッドの説明は以下のサイトが分かりやすいです  
 　[note.nkmk.me](https://note.nkmk.me/pandas/)  
・"Data for Titanic passengers" from [VANDERBILT UNIVERSITY](https://biostat.app.vumc.org/wiki/Main/DataSets)  
  
**本コンテンツ作成時のpandasのバージョンは1.1.0**
  
作成日:2020年9月24日  
最終更新日:203年1月16日  
再配布・改編不可  
作成者：[kunishou](https://qiita.com/kunishou)
"""

# %%
# Shift + Enterで題材データ、回答コードを読み込んで下さい

import pandas as pd
import glob
import random

#題材データをdfに読み込み(タイタニック号の乗客データ、テストの点数データ 等)
def initialize1():
    df = pd.read_csv('../input/titanic3.csv')
    return df

def initialize2():
    df = pd.read_csv('../input/data1.csv')
    return df

df = initialize1()
df2 = initialize2()
df3 = pd.read_csv('../input/data1_2.csv')
df4 = pd.read_csv('../input/data1_3.csv')
df5 = pd.read_csv('../input/data2.csv',encoding='cp932')

#問題文をquesリストに格納
path = sorted(glob.glob('../input/q_' + '*.txt'))

ques = []

for _ in range(len(path)):
    with open(path[_], 'r',encoding='utf-8') as f:
        ques.append(f.read())

#回答コードをansリストに格納
path2 = sorted(glob.glob('../input/a_' + '*.txt'))

ans = []

for _ in range(len(path)):
    with open(path2[_], 'r',encoding='utf-8') as f:
        ans.append(f.read())

print(ques[0])
print(ans[0])

# %% [markdown]
"""
# Random Knocks
"""

# %%
#問題をランダムに表示
print(random.choice(ques[1:]))

# %%
df = initialize1() # 初期化
df2 = initialize2() # 初期化
# 回答をここに記述





# %%
#print(ans[]) # 回答表示(ans[]の[]内に問題番号を記入)

# %% [markdown]
"""
各セルのoutput表示をすべてクリアにしたい場合は、ツールバーの  
「Kernel」→「Restart & Clear Output」を実行して下さい。
"""

