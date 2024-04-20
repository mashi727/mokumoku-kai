import dash
from dash import html
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
app.layout = html.Div([
    # htmlの<button>タグにInputで使うid属性を指定する
    html.Button('Submit', id='button-example-1'),
    # htmlの<div>タグにOutputで使うid属性を指定する
    html.Div(id='output-value', children='counter-value')
])


@app.callback(
    # Outputで戻り値の出力先を指定する
    # ボタンがクリックされると<div>タグに値が渡されて、数値が増えていくカウンターが表示される
    Output('output-value', 'children'),
    # コールバックの呼び出し要素の指定
    Input('button-example-1', 'n_clicks'))
# ボタンがクリックされると属性が変化して、処理が呼び出される
def update_output(n_clicks):
    # 返り値を返す
    return n_clicks


if __name__ == '__main__':
    app.run_server(debug=True)	
