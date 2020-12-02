"""
Module with single function to clean data file
"""

#will add a function to get data file from gdrive

#will add a function to "flatten" data so that there is one row per project

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

    return data
