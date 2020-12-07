import pandas as pd
import os

""" Simple module to read in data

Will be edited in the future to deal with larger filesizes, possibly g-drive.
Serves as a placeholder so other components can call.
"""

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/project_db_1000.csv')
print(filename)

def get_data():
    data = pd.read_csv(filename, low_memory=False)
    return data