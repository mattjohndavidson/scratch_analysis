import pandas as pd

""" Simple module to read in data

Will be edited in the future to deal with larger filesizes, possibly g-drive.
Serves as a placeholder so other components can call.
"""

def get_data():
    data = pd.read_csv('data/project_db_1000.csv',low_memory=False)
    return data