import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import requests
from datetime import datetime

app = dash.Dash()

headers = {'Authorization': 'Token e9e301d24df5800184e89343cf47381b', 'Content-Type': 'application/json'}
response = requests.get("https://api.oilpriceapi.com/v1/prices/latest", headers=headers).json()


now = datetime.now()
X = deque(maxlen=20)
X.append(now.strftime("%H:%M:%S"))
Y = deque(maxlen=20)
Y.append(response["data"]["price"])

app.layout = html.Div(
    [
        html.H1('Oil Price live update'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*30000,
            n_intervals=0
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'), [Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
    
    response = requests.get("https://api.oilpriceapi.com/v1/prices/latest", headers=headers).json()
    now = datetime.now()

    X.append(now.strftime("%H:%M:%S"))
    Y.append(response["data"]["price"])

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data], 'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)