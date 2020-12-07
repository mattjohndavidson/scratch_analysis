import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_daq as dash_daq
from dash.dependencies import Input, Output, State
import os
import clean_data as cdt
import search

"""
Sorts data based on inputs.
"""

# Load the data
data = cdt.clean_columns(pd.read_csv('data/project_db_1000.csv',low_memory=False))

popularity_grades = data.groupby('project_ID').first()
blocks_flattened = data.groupby(['project_ID'])['block_type'].value_counts().unstack(fill_value=0).reset_index()
merged = popularity_grades.merge(blocks_flattened, left_on='project_ID', right_on='project_ID', how = 'left')
removed_columns = np.array(['script_ID','project_ID','project_name','is_remix','block_rank','Clones','InstancesSprites'])

columns = np.setdiff1d(data.columns.values,removed_columns)
block_types = np.setdiff1d(np.array(merged.columns.values),np.array(data.columns.values))

# block_options = {}
# for col in columns:
#     block_options[col] = []
# block_options['block_type'] = block_types

# begin app
app = dash.Dash(__name__)
app.layout = html.Div(style={'textAlign': 'center', 'width': '800px', 'font-family': 'Verdana'},

    children = [    
    # title
    html.H1("Search for scratch projects that fit your needs!"),
    
    html.H2('Search metric:'),

    #dropdown menu to choose feature importance graph based on one of 4 labels
    dcc.Dropdown(
        id='search-dropdown',
        options=[
            {'label': 'Total blocks', 'value': 'total_blocks'},
            {'label': 'Total remixes', 'value': 'total_remixes'},
            {'label': 'Total views', 'value': 'total_views'},
            {'label': 'Total favorites', 'value': 'total_favorites'},
            {'label': 'Total loves', 'value': 'total_loves'},
            {'label': 'Block type', 'value': 'block_type'},
            {'label': 'Abstraction', 'value': 'Abstraction'},
            {'label': 'Parallelism', 'value': 'Parallelism'},
            {'label': 'Logic', 'value': 'Logic'},
            {'label': 'Synchronization', 'value': 'Synchronization'},
            {'label': 'Flow control', 'value': 'FlowControl'},
            {'label': 'User interactivity', 'value': 'UserInteractivity'},
            {'label': 'Data representation', 'value': 'DataRepresentation'},
            {'label': 'Mastery', 'value': 'Mastery'},
        ],
        value = 'total_blocks'
    ),
        
    dcc.Checklist(id='block-checklist'),

#         options = [{'label': block, 'value': block} for block in block_types],
#         labelStyle={'display': 'inline-block'}
#     ),
        
    html.Button(id='search-button', n_clicks=0, children='Search'),
        
    html.Hr(),
        
    html.H2('Search result:'),

    html.Div(id='output-url'),
        
    html.Button(id='search-update', n_clicks=0, children='Update')
])


@app.callback(
    Output('block-checklist', 'options'),
    Input('search-dropdown', 'value'))
def set_block_options(selected_search):
    if selected_search == 'block_type':
        block_options = [{'label': block, 'value': block} for block in block_types]
    else:
        block_options = []
        
    return block_options


# @app.callback(
#     Output('block-checklist', 'value'),
#     Input('block-checklist', 'options')),
# def set_block_values(available_options):
#     return available_options[0]['value']


@app.callback(
    Output('output-url','children'),
    Input('search-button', 'n_clicks'),
    State('search-dropdown', 'value'),
    State('block-checklist', 'value'))
def update_scratch(n_clicks, input1, input2):
    sorted_data = search.search_data(data, input1, input2)
    p_id = sorted_data.iloc[0].project_ID
    
    return u'Project URL: https://scratch.mit.edu/projects/{}'.format(p_id)


if __name__ == '__main__':
    app.run_server(debug=True)
