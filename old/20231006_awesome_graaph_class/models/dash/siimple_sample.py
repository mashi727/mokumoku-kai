import dash
from dash import dcc
from dash import html

# Dashインスタンスを生成する
app = dash.Dash(__name__)
# コンポーネントをlayout属性に渡す
app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    # スタイルの設定
    style={
        "fontSize": 50,  # 文字サイズ
        "color": "white",  # 文字色
        "backgroundColor": "#000000",  # 背景色
    },
)

if __name__ == "__main__":
# アプリケーションを起動する
    app.run_server(debug=True)
