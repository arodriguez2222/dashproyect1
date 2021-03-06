# Load your libraries
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

from deep_translator import GoogleTranslator

# Create the app

#workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
request_path_prefix = None
#if workspace_user:
#request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'
request_path_prefix = '/user/proxy/8050/'

app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'Translator - Correlation One'  

# Layout
app.layout = dbc.Container([
    html.H1(["Google Translator"],  className="h-100 p-5 bg-light border rounded-3"),
    dbc.Input(id="my-input", placeholder="Type something", type="text", value="home"),
    html.Br(),
    html.P(id="my-output", children=['home'])
])

# Callback
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    translated_input_text = GoogleTranslator(source='auto', target='es').translate(input_value) 
    return 'Your translation:  "{}"'.format(translated_input_text)

# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)