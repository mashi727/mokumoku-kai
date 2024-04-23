# 作業メモ


## 2024.4.24

フォルダの整理を行いました。

### フォルダやファイルを追加する際のポリシー

- プロトタイピングやテストコードは`small_works`にフォルダを作成して入れるようにしましょう。
- フォルダを作成した際は、目的などを記述したREADME.mdを作成してください。
- 実際に運用するツールは、portfolioにフォルダを作成して格納します。

#### 現在のフォルダ構成

フォルダの構成は、以下の通り。
<details><summary>フォルダ構成</summary>

```sh
.
├── Learning
│   └── Books
├── old
│   ├── 20231006_awesome_graaph_class
│   ├── backtest_old
│   └── backtest_samples_from_pypi
├── portfolio
└── small_works
    ├── convert_one-min_to_any-min
    ├── convert_one-min_to_volume
    ├── hdf5_test
    └── reliability_test_for_stockdata

13 directories
```

</details>


### Action Item


#### stockデータ検証（reliability_test_for_stockdata）

stockデータは、Alpha VantageとYahoo Financeから行なっています。
現在の方針は、1min足を収集、記録して、任意の足（5min, 60min, 1dayなど）は1min足から計算する方向を検討しています。

それぞれ無料で利用していますが、それぞれ以下の制約があります。

Yahooは、1min足は一週間前までのデータのみ収集可能。
Alpha Vantageは、1ヶ月分のデータを収集可能ですが1日25回までしか取得できない。


同じ会社の株式を比較して問題なければ、今後はYahooで指定銘柄を毎日記録することとしようかと考えています。



#### 1min足から、任意の足を作成

これも、検証が必要です。
リサンプルで、5min足へ変換するコードをネットで拾ってきましたが。
理解と検証が必要です。
rule(rule)を10T、1Hなど変更すれば、任意の足に変換可能です。

```python
df_five = pd.DataFrame()
rule = "5T"
df_five["Open"] = df_one["Open"].resample(rule).first()
df_five["Close"] = df_one["Close"].resample(rule).last()
df_five["High"] = df_one["High"].resample(rule).max()
df_five["Low"] = df_one["Low"].resample(rule).min()
```


#### データの保存について(hdf5_test)

データの保存は悩ましいところです。
方法としては、SQLを使用してデータベースを作成する方法と、`hdf5`を利用する方法があります。
現状は、最も遅く煩雑になりやすい`csv`でフォルダ管理を行なっています。

現時点での結論としては、`hdf5`を使用する方向でテストを行います。

理由は、以下の通り。

- 一つのファイルで構造データを管理できる。
    - 興味のある企業ごとにStock dataと財務諸表などのファンダメンタルデータを保存する必要があるため必須。
- 高速である。（要検証）
- 学術分野における大容量データの扱い（MLなど）において実績がある。



## 2024.4.20

環境構築のお手伝いに伴う最低限のファイルをアップロード


覚えた方が望ましいこと
- `git pull`で、最新の状態に更新。どこのフォルダで実行しても問題ありません。

