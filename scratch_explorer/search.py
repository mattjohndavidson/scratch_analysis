"""Contains function to search scratch data."""

import numpy as np
import pandas as pd


def search_data(data, column, block_search=np.array([None])):
    """Searches cleaned dataframe based on the column input by the user.

    Params
    --------
    data: pandas dataframe with data from scratch_analysis.csv
    column: column to sort by
    block_type: if column = block_type, block_type defines which block_types
                to include in the search, default is None

    Returns
    --------
    sorted_data: pandas sorted dataframe sorted by user choice.
    """
    if not isinstance(column, str):
        raise ValueError('Bad input. Column must be a string.')
    else:
        pass
    if block_search is None:
        pass
    elif not all(isinstance(block, str) for block in block_search):
        raise ValueError('Bad input. block_types must be strings.')
    else:
        pass

    REMOVED_COLUMNS = np.array(['p_ID', 'project_name', 'CustomBlocks',
                                'is_remix', 'Clones'])

    ALL_SEARCH_COLUMNS = np.append(
                            np.setdiff1d(data.columns.values, REMOVED_COLUMNS),
                            ['block-type'])

    NON_BLOCK_COLUMNS = np.array(['total-views', 'total-remixes',
                                  'total-favorites', 'total-loves',
                                  'Abstraction', 'Parallelism',
                                  'Logic', 'Synchronization',
                                  'FlowControl', 'UserInteractivity',
                                  'DataRepresentation', 'Mastery',
                                  'total-blocks', 'block-type'])

    BLOCK_TYPES = np.setdiff1d(ALL_SEARCH_COLUMNS, NON_BLOCK_COLUMNS)

    err1 = 'Bad input. To search by block type, input a block type to search.'
    err2 = 'Bad input. Must search by valid block type values.'
    if column not in NON_BLOCK_COLUMNS:
        raise ValueError('Bad input. Column must be a search parameter.')
    elif column == 'block-type':
        if block_search is None or len(block_search) == 0:
            raise ValueError(err1)
        elif not all(block in BLOCK_TYPES for block in block_search):
            raise ValueError(err2)
        elif len(block_search) == 1:
            search_term = block_search[0]
        else:
            block_search_sum = sum([data[block] for block in block_search])
            if 'search_sum' in data.columns.values:
                data = data.drop(columns=['search_sum'])
            data.insert(len(data.columns), 'search_sum', block_search_sum)
            search_term = 'search_sum'
    else:
        search_term = column

    sorted_data = data.sort_values(search_term, ascending=False)

    return sorted_data
