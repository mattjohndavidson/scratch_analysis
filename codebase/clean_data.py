import pandas as pd
import numpy as np

def clean_data(data):
    #replacing dashes with underscores
    data.columns = [i.replace('-', '_') for i in data.columns]

    #removing redundant columns
    data = data.drop(columns=['Script_ID','p_ID'])

    #remove unnecessary columns
    data = data[data.columns[~data.columns.str.contains('param')]]

    return(data)