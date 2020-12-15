"""
initial combination of two function
"""
import os
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import clean_data as cdt
import search
import joblib



# Load the data
file_name = 'data/scratch_data.csv'
data = pd.read_csv(file_name, low_memory=False).drop(columns=['Unnamed: 0'])

dirname = os.path.dirname(__file__)
filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
filename_features = os.path.join(dirname, 'exports/feature_list.sav')
model = joblib.load(filename_model)
feature_list = joblib.load(filename_features)

removed_columns = np.array(['p_ID', 'project_name', 'CustomBlocks',
                            'is_remix', 'Clones'])

all_search_columns = np.setdiff1d(data.columns.values, removed_columns)

non_block_columns = np.array(['total-views', 'total-remixes',
                              'total-favorites', 'total-loves',
                              'Abstraction', 'Parallelism',
                              'Logic', 'Synchronization',
                              'FlowControl', 'UserInteractivity',
                              'DataRepresentation', 'Mastery',
                              'total-blocks'])

block_types = np.setdiff1d(all_search_columns, non_block_columns)

# begin app
app = dash.Dash(__name__)
app.layout = html.Div(style={'textAlign': 'center', 'width': '800px', 'font-family': 'Verdana'},

                      children=[
                          # title
                          html.H1("Scratch Analysis"),
                          html.Br(),
                          dcc.Tabs([
                              dcc.Tab(label = "Search Function", children = [
                                                          html.H2("1.Search for scratch projects that fit your needs!"),

                          html.H3('Search metric:'),

                          #dropdown menu to choose feature importance graph based on one of 4 labels
                          dcc.Dropdown(
                              id='search-dropdown',
                              options=[
                                  {'label': 'Total blocks', 'value': 'total-blocks'},
                                  {'label': 'Total remixes', 'value': 'total-remixes'},
                                  {'label': 'Total views', 'value': 'total-views'},
                                  {'label': 'Total favorites', 'value': 'total-favorites'},
                                  {'label': 'Total loves', 'value': 'total-loves'},
                                  {'label': 'Block type', 'value': 'block-type'},
                                  {'label': 'Abstraction', 'value': 'Abstraction'},
                                  {'label': 'Parallelism', 'value': 'Parallelism'},
                                  {'label': 'Logic', 'value': 'Logic'},
                                  {'label': 'Synchronization', 'value': 'Synchronization'},
                                  {'label': 'Flow control', 'value': 'FlowControl'},
                                  {'label': 'User interactivity', 'value': 'UserInteractivity'},
                                  {'label': 'Data representation', 'value': 'DataRepresentation'},
                                  {'label': 'Mastery', 'value': 'Mastery'},
                                  ],
                              value='total-blocks'
                              ),

                          dcc.Checklist(id='block-checklist'),

                          html.Button(id='search-button', n_clicks=0, children='Search'),

                          html.Hr(),

                          html.H3('Search result:'),

                          html.A(id='output-url', children='Project source code', target='_blank'),

                          html.Iframe(
                              id='scratch',
                              style={'border': 'none', 'width': '100%', 'height': 500},
                              src='https://scratch.mit.edu/projects/98698671/embed'
                              ),

                          html.Button(id='update-button', n_clicks=0, children='Update')
                              ]),
                          

                          dcc.Tab(label = "popularity metric", children = [
html.H2("2.See which features were most predictive of the chosen popularity metric"),

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

                          dcc.Graph(id='figure_importances')
                          ]),
                          ]),
                          ]
                      )


@app.callback(
    Output('block-checklist', 'options'),
    Input('search-dropdown', 'value'))
def set_block_options(selected_search):
    if selected_search == 'block_type':
        block_options = [{'label': block, 'value': block} for block in block_types]
    else:
        block_options = []

    return block_options


@app.callback(
    Output('output-url', 'href'),
    Output('scratch', 'src'),
    Input('search-button', 'n_clicks'),
    Input('update-button', 'n_clicks'),
    State('search-dropdown', 'value'),
    State('block-checklist', 'value'))
def update_scratch(search_clicks, update_clicks, input1, input2):
    clicked_button = [p['prop_id'] for p in dash.callback_context.triggered][0]
    sorted_data = search.search_data(data, input1, input2)

    if 'search-button' in clicked_button:
        p_id = sorted_data.iloc[0].p_ID
    elif 'update-button' in clicked_button:
        p_id = sorted_data.iloc[update_clicks].p_ID

    href = 'https://scratch.mit.edu/projects/{}/editor/'.format(p_id)
    src = 'https://scratch.mit.edu/projects/{}/embed'.format(p_id)

    return href, src


@app.callback(
    Output('update-button', 'n_clicks'),
    Input('search-button', 'n_clicks'))
def reset_update(n_clicks):
    return 0


@app.callback(
    Output('figure_importances', 'figure'),
    [Input('labels-dropdown', 'value')])
def update_graph(outcome):
    feature_imps = pd.DataFrame(model.estimators_[outcome].feature_importances_,
                                columns=["Importance"], index=feature_list)
    feature_imps = feature_imps.sort_values("Importance", ascending=False)

    fig = px.bar(x=feature_imps["Importance"][:10], y=feature_imps.index[:10], orientation='h',
                 range_x=(0, .25),
                 labels={
                     'x' : 'Feature Importance',
                     'y' : 'Feature Name'
                 })
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
