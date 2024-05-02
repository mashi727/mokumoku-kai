# %% [markdown]
"""
# タイタニック号乗客の生存予測ver1.0.7
##### 90～100を通しで実行する場合のサンプルコード
##### Shift + Enter で各セルのコードが実行されます
・print(ans[ 問題番号 ]) で回答コード例を表示  
・Python3エンジニア認定データ分析試験にも沿った問題内容   
・Pandasの各メソッドの説明は以下のサイトが分かりやすいです  
 　[note.nkmk.me](https://note.nkmk.me/pandas/)  
・"Data for Titanic passengers" from [VANDERBILT UNIVERSITY](https://biostat.app.vumc.org/wiki/Main/DataSets)  
  
**本コンテンツ作成時のpandasのバージョンは1.1.0**
  
作成日:2020年9月24日  
再配布・改編不可  
作成者：[kunishou](https://qiita.com/kunishou)
"""

# %%
import pandas as pd

# データの読み込み
df = pd.read_csv('../input/titanic3.csv')

df_copy = df.copy()

# ラベルエンコーディング
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder() #ラベルエンコーダのインスタンスを作成

df_copy['sex'] = le.fit_transform(df_copy['sex']) #エンコーディング
df_copy['embarked'] = le.fit_transform(df_copy['embarked'].astype(str))

# 欠損値補完
df_copy['age'] = df_copy['age'].fillna(df_copy['age'].median()) #欠損値にageの平均値で補完
df_copy['fare'] = df_copy['fare'].fillna(df_copy['fare'].median()) #欠損値にfareの平均値で補完

# 不要行の削除
df_copy = df_copy.drop(['name', 'ticket', 'cabin', 'boat', 'body', 'home.dest'],axis=1)

# ndarray形式への変換
features = df_copy[['pclass','age','sex','fare','embarked']].values
target = df_copy['survived'].values

# 学習データとテストデータに分割
from sklearn.model_selection import  train_test_split

(features , test_X , target , test_y) = train_test_split(features, target , test_size = 0.3 , random_state = 0)

# 学習
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100,random_state=0) # ランダムフォレストのインスタンスを作成

model.fit(features,target) # 学習の実行

# 予測
pred = model.predict(test_X)

# 予測精度の確認
from sklearn.metrics import accuracy_score

print(accuracy_score(pred,test_y))

# 重要度の表示
importance = model.feature_importances_ 

print('Feature Importances:')
for i, feat in enumerate(['pclass','age','sex','fare','embarked']):
    print('\t{0:20s} : {1:>.5f}'.format(feat, importance[i]))
    
# csvで出力
df_pred = pd.DataFrame(pred)
df_pred.to_csv('../output/submission.csv',header=None)

