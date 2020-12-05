"""
Module with functions to clean data file
"""

#will add a function to "flatten" data so that there is one row per project
def flatten_data(data):
    """
    Takes "long" data file as input, returns "wide" df with one row per project
    """

    popularity_grades = data.groupby('project_ID').first()
    blocks_flattened = data.groupby(['project_ID'])['block_type'].value_counts().unstack(fill_value=0).reset_index()
    merged = popularity_grades.merge(blocks_flattened, left_on='project_ID', right_on='project_ID', how = 'left')
    return merged

def clean_columns(data):
    """
    Cleans up data file for further processing. 
    """

    #replacing dashes with underscores
    data.columns = [i.replace('-', '_') for i in data.columns]

    #removing redundant columns
    data = data.drop(columns=['Script_ID', 'p_ID'])

    #remove unnecessary columns
    data = data[data.columns[~data.columns.str.contains('param')]]
    data = data.drop(columns=['sprite_type','sprite_name','script_rank','coordinates','username','project_ID.1','Script_ID','p_ID'])

    return data
