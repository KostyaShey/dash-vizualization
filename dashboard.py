import dash
import dash_core_components as dcc
import dash_html_components as html

#function for the first CI step
def addtwonumbers(int_a, int_b):
    return int_a + int_b

App = dash.Dash()

App.layout = html.Div(children=[html.H1(children='Dash Tutorials'),\
    dcc.Graph(id='example',\
        figure={'data': [\
            {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 9, 9, 9], 'type': 'line', 'name': 'Boats'},\
            {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},],\
                'layout': {'title': 'Basic Dash Example'}})])

if __name__ == '__main__':
    App.run_server(debug=True)
    