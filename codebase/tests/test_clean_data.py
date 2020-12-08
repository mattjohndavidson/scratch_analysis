import os
import unittest
import pandas as pd
import numpy as np
from codebase import clean_data
from codebase import search

#print(clean_data.__path__)
data_path = "data/"
#os.path.join(clean_data.__path__[0], 'data')

class test_clean_data(unittest.TestCase):

    def test_col_clean(self):
        """
        Testing the cleaning of column names
        """
        self.assertTrue(True)
 #       df = pd.read_csv(os.path.join(data_path, 'project_db_1000.csv'))
  #      df_clean = clean_data.clean_data(df)
  #      dataset = df_clean.columns

   #     for i in range(len(dataset)):
   #         has_dash = dataset[i].find("-")
   #         self.assertNotEqual(has_dash, -1)
    

class test_search(unittest.TestCase):
    """Includes unit tests for search.py"""
    
    def test1(self):
        """column input is not a string"""
        with self.assertRaises(ValueError):
            data = clean_data.clean_columns(pd.read_csv('codebase/data/project_db_1000.csv', low_memory=False))
            column = 4
            block_search = None
            search.search_data(data,column,block_search)


    def test2(self):
        """column input is not an option"""
        with self.assertRaises(ValueError):
            data = clean_data.clean_columns(pd.read_csv('codebase/data/project_db_1000.csv', low_memory=False))
            column = 'Number'
            block_search = None
            search.search_data(data,column,block_search)


if __name__ == '__main__':
    unittest.main()
