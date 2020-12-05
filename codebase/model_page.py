import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_daq as dash_daq
from dash.dependencies import Input, Output

"""
Reads in saved model object; creates dash page

"""

#loading the fitted model object
model = joblib.load('exports/fitted_model.sav')
feature_list = joblib.load('exports/feature_list.sav')
#create the default feature importance graph
def get_feature_graph(label):
    """
    Creates a graph of feature importance based on passed in label
    """
    feature_imps = pd.DataFrame(model.estimators_[label].feature_importances_*100,columns=["Importance"],index=feature_list)
    feature_imps = feature_imps.sort_values("Importance", ascending=False)[-10:]

    fig_features_importance = go.Figure()
    fig_features_importance.add_trace(go.Bar(x = feature_imps["Importance"],
                                            y = feature_imps.index,
                                            orientation = 'h',
                                            marker_color = 'rgb(171, 226, 251)'))
    fig_features_importance.update_layout(title_text = '<b>Importance of features in the model<b>', title_x = 0.5)
    return fig_features_importance

# begin app

app = dash.Dash(__name__)
app.layout = html.Div(
    children = [
        # title
        html.H1("See which features were most predictive of the chosen popularity metric"),
            
        dcc.Graph(figure=get_feature_graph(0)),
        
        #dropdown menu to choose feature importance graph based on one of 4 labels
        dcc.Dropdown(
            id='labels-dropdown',
            options=[
                {'label': 'Total remixes', 'value': '0'},
                {'label': 'Total views', 'value': '1'},
                {'label': 'Total favorties', 'value': '2'},
                {'label': 'Total loves', 'value': '3'}
            ],
            value='0'
        ),
        html.Div(id='dd-output-container')
    ]
)


@app.callback(
    Output('dd-output-container', 'children'),
    [Input('labels-dropdown', 'value')])
def update_graph(value):
    fig = get_feature_graph(value)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
