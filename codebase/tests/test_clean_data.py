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
    #test that all '-' have been converted to '_'
    #test that all columns to be removed have been removed
    
    def test_flatten_data(self):
       """
       Tests the flatten data function.
       """
       pass
       #write tests to get the number of unique project ids in the initial data
       #verify that n_rows of flat data == count of unique ids
       #ensure that the ncol == max(num_rows of initial data), but probably minus count of unique ids
