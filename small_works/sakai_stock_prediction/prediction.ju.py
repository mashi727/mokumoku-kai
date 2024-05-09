# %% [markdown]
"""

# scikit-learnで機械学習を行う

機械学習のお試し的に、scikit-learnで株価の予測をやってみます。
酒井さんの本は、公式ドキュメントの読み方からの読み取りのプロセスが書いてあるので、とても良いと思う。


"""
# %%
import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection
import matplotlib.pyplot as plt
import pandas as pd

diabetes = sklearn.datasets.load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

diabetes.target

x = diabetes.data
y = diabetes.target


X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

lr = sklearn.linear_model.LinearRegression()
lr.fit(X_train, y_train)
lr.score(X_test, y_test)

predicted = lr.predict(x)
fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], "k--", lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()


# %% [markdown]


# %%

