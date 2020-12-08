"""Creates a dash app for the search function."""

import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import clean_data as cdt
import search


# Load the data
data = cdt.clean_columns(pd.read_csv('data/project_db_1000.csv', low_memory=False))

popularity_grades = data.groupby('project_ID').first()
blocks_flattened = data.groupby(['project_ID'])['block_type'].value_counts().unstack(fill_value=0).reset_index()
merged = popularity_grades.merge(blocks_flattened, left_on='project_ID', right_on='project_ID', how='left')
removed_columns = np.array(['script_ID', 'project_ID', 'project_name',
                            'is_remix', 'block_rank', 'Clones', 'InstancesSprites'])

columns = np.setdiff1d(data.columns.values, removed_columns)
block_types = np.setdiff1d(np.array(merged.columns.values), np.array(data.columns.values))

# begin app
app = dash.Dash(__name__)
app.layout = html.Div(style={'textAlign': 'center', 'width': '800px', 'font-family': 'Verdana'},

    children=[
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
            value='total_blocks'
        ),

        dcc.Checklist(id='block-checklist'),

        html.Button(id='search-button', n_clicks=0, children='Search'),

        html.Hr(),

        html.H2('Search result:'),

        html.A(id='output-url', children='Project source code', target='_blank'),

        html.Iframe(
            id='scratch',
            style={'border': 'none', 'width': '100%', 'height': 500},
            src='https://scratch.mit.edu/projects/98698671/embed'
        ),

        html.Button(id='update-button', n_clicks=0, children='Update')
    ]
)


@app.callback(
    Output('block-checklist', 'options'),
    Input('search-dropdown', 'value'))
def set_block_options(selected_search):
    """Adds block types when block_types is selected"""
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
    """Updates scratch project for each search"""
    clicked_button = [p['prop_id'] for p in dash.callback_context.triggered][0]
    sorted_data = search.search_data(data, input1, input2)

    if 'search-button' in clicked_button:
        p_id = sorted_data.iloc[0].project_ID
    elif 'update-button' in clicked_button:
        p_id = sorted_data.iloc[update_clicks].project_ID

    href = 'https://scratch.mit.edu/projects/{}/editor/'.format(p_id)
    src = 'https://scratch.mit.edu/projects/{}/embed'.format(p_id)

    return href, src


@app.callback(
    Output('update-button', 'n_clicks'),
    Input('search-button', 'n_clicks'))
def reset_update(n_clicks):
    """Resets the update counter"""
    return 0


if __name__ == '__main__':
    app.run_server(debug=True)
