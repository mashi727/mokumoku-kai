# -*- coding: utf-8 -*-
import dash

from dash import dash_table
from dash import dcc
from dash import html

import pandas as pd

app = dash.Dash()


app.layout = html.Div(children=[
html.Div(children='LinuxHint Youtube Hi'),
dcc.Graph(
id='graphss',
figure={
'data': [
{'x':[1,2,3,4,5,6,7], 'y':[11,12,22,23,24,44,55], 'type':'line', 'name':'Energy'},
{'x':[1,2,3,4,5,6,7], 'y':[13,15,26,27,34,44,65], 'type':'bar', 'name':'Time'},
],
'layout': {
'title': 'Graph for Time and Energy'
}
}
)
])

if __name__ == '__main__':
    app.run_server(debug=True)
