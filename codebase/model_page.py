import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_daq as dash_daq
from dash.dependencies import Input, Output
import os

"""
Reads in saved model object; creates dash page
"""

#loading the fitted model object
dirname = os.path.dirname(__file__)
filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
filename_features = os.path.join(dirname, 'exports/feature_list.sav')
model = joblib.load(filename_model)
feature_list = joblib.load(filename_features)

# begin app
app = dash.Dash(__name__)
app.layout = html.Div(style={'textAlign': 'center', 'width': '800px', 'font-family': 'Verdana'},

    children = [    
    # title
    html.H1("See which features were most predictive of the chosen popularity metric"),

    #dropdown menu to choose feature importance graph based on one of 4 labels
    dcc.Dropdown(
        id='labels-dropdown',
        options=[
            {'label': 'Total remixes', 'value': 0},
            {'label': 'Total views', 'value': 1},
            {'label': 'Total favorties', 'value': 2},
            {'label': 'Total loves', 'value': 3}
        ],
        value=0
    ),

    dcc.Graph(id = 'figure_importances')
])

@app.callback(
    Output('figure_importances', 'figure'),
    [Input('labels-dropdown', 'value')])
def update_graph(outcome):
    feature_imps = pd.DataFrame(model.estimators_[outcome].feature_importances_,columns=["Importance"],index=feature_list)
    feature_imps = feature_imps.sort_values("Importance", ascending=False)

    fig = px.bar(x = feature_imps["Importance"][:10], y = feature_imps.index[:10], orientation='h',
                 range_x=(0, .25),
                 labels={
                     'x' : 'Feature Importance',
                     'y' : 'Feature Name'
                 })
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
