import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

def generate_dropdown_options():
    
    dropdown_options = []
    df_options = pd.read_csv('USvideos.csv')
    df_options = df_options[["title", "video_id"]]
    df_options.drop_duplicates(inplace = True)
    df_options.columns = ['label','value']
    for index, row in df_options.iterrows():
        dropdown_options.append(row.to_dict())
    return dropdown_options


app.layout = html.Div(children=[
    html.Div(children='''
        Video to graph:
    '''),
    dcc.Dropdown(
        id='my-dropdown',
        options=generate_dropdown_options(),
        value="",
        placeholder="Select a video"
    ),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='my-dropdown', component_property='value')]
)
def update_value(input_data):

    df = pd.read_csv('USvideos.csv')
    df.reset_index(inplace=True)
    df = df[df["video_id"] == input_data]
    df.reset_index(inplace=True)
    if input_data != "":
        title_for_graph = "Views per day for " + str(df["title"].unique()[0])

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df["trending_date"], 'y': df["views"], 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': title_for_graph
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)