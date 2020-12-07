import numpy as np
import pandas as pd

def search_data(data, column, block_search=np.array([None])):
    """Searches cleaned dataframe based on the column input by the user.

    Params
    --------
    data: pandas dataframe cleaned with clean_data.py
    column: column to sort by
    block_type: if column = block_type, block_type defines which block_types to include in the search, default is None
    
    Returns
    --------
    sorted_data: pandas sorted dataframe sorted by user choice.
    """
    if not isinstance(column,str):
        raise ValueError('Bad input. Column must be a string.')
    else:
        pass
    if block_search is None:
        pass
    elif not all(isinstance(block,str) for block in block_search):
        raise ValueError('Bad input. block_types must be strings.')
    else:
        pass

    popularity_grades = data.groupby('project_ID').first()
    blocks_flattened = data.groupby(['project_ID'])['block_type'].value_counts().unstack(fill_value=0).reset_index()
    merged = popularity_grades.merge(blocks_flattened, left_on='project_ID', right_on='project_ID', how = 'left')

    removed_columns = np.array(['script_ID','project_ID','project_name','is_remix','block_rank','Clones','InstancesSprites'])
    columns = np.setdiff1d(data.columns.values,removed_columns)
    block_types = np.setdiff1d(np.array(merged.columns.values),np.array(data.columns.values))

    if column not in columns:
        raise ValueError('Bad input. column must be a column of the dataframe.')
    elif column == 'block_type':
        if block_search is None or len(block_search) == 0:
            raise ValueError('Bad input. To search by block type, input a block type to search.')
        elif not all(block in block_types for block in block_search):
            raise ValueError('Bad input. Must search by valid block_type values.')
        elif len(block_search) == 1:
            search_term = block_search[0]
        else:
            block_search_sum = sum([merged[block] for block in block_search])
            merged.insert(len(merged.columns),"search_sum",block_search_sum)
            search_term = 'search_sum'
    else:
        search_term = column

    sorted_data = merged.sort_values(search_term,ascending=False)

    return sorted_data