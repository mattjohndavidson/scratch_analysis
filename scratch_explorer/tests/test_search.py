import os
import unittest
import pandas as pd
import numpy as np
from scratch_explorer import search


class test_search(unittest.TestCase):
    """Includes unit tests for search.py"""
    
    def test1(self):
        """column input is not a string"""
        with self.assertRaises(ValueError):
            data = pd.read_csv('scratch_explorer/data/scratch_sample.csv', low_memory=False).drop(columns=['Unnamed: 0'])
            column = 4
            block_search = None
            search.search_data(data,column,block_search)


    def test2(self):
        """column input is not an option"""
        with self.assertRaises(ValueError):
            data = pd.read_csv('scratch_explorer/data/scratch_sample.csv', low_memory=False).drop(columns=['Unnamed: 0'])
            column = 'Number'
            block_search = None
            search.search_data(data,column,block_search)


if __name__ == '__main__':
    unittest.main()
