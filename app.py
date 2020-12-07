"""
simple app to show the dataset

different algorithms to be added later with pages
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'codebase/data/project_db_1000.csv')
available_indicators = df['block-type'].unique()
app = dash.Dash(__name__)

app.layout = html.Div(
    [
    html.H1("Scratch Analysis"),
    html.Br(),
    html.H2("1.Search Function"),
    dcc.Input(id="search", type="text", placeholder="Enter type of block"),
    html.Div(id="Search output"),
    html.Br(),
    html.H2("2.ML Module"),
    html.Div([
            dcc.Dropdown(
                id='blocks',
                options=[{'label': i, 'value': i} for i in available_indicators],
            ),
            ]),
    dcc.Graph(id='ML output'),
    ]
)

@app.callback(
    Output("Search output", "children"),
    Input("search", "value")
)
def search_fun(search):
    return("Search result: ", search)

@app.callback(
    Output("ML output", "children"),
    Input("blocks", "value")
)
def ML_fun(bloc):
    dff = df[df['block-type'] == bloc]
    fig = px.scatter(dff, x = dff['block-rank'], y= dff['total-views'])
    return fig
    
if __name__ == '__main__':
    app.run_server(debug=True)