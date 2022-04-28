# Load your libraries
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

import plotly.express as px
from dash.dependencies import Input, Output

from deep_translator import GoogleTranslator

# Create the app

workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
request_path_prefix = None
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'Bars - Correlation One'  

# Layout
app.layout = dbc.Container(children=[
    html.H1(['Correlation-One / DS4A Team'], className="display-2 h-100 p-5 text-white bg-dark rounded-3"),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Div([
        dbc.Input(id="my-input", placeholder="Type something...", type="text"),
        html.Br(),
        html.P(id="my-output")
    ])
])

# Callback
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    translated_input_text = ""
    if input_value:
        translated_input_text = translator.translate(input_value,lang_tgt='es')
    return 'Your translation:  "{}"'.format(translated_input_text)


# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)