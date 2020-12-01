import os
import unittest
import pandas as pd
import numpy as np
import clean_data

data_path = os.path.join(codebase.__path__[0], 'data')

class test_clean_data(unittest.TestCase):

    def test_col_clean(self):
        """
        Testing the cleaning of column names
        """
        df = pd.read_csv(os.path.join(data_path, 'project_db_1000.csv'))
        clean_dat = clean_data(df)
        dataset = df.columns

        for i in range(len(dataset)):
            has_dash = dataset[i].find("-")
            self.assertNotEqual(has_dash, -1)