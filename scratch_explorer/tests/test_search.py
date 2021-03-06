"""Unit tests for search.py"""

import unittest
import pandas as pd
from scratch_explorer import search


class test_search(unittest.TestCase):
    """Includes unit tests for search.py"""
    data = pd.read_csv('scratch_explorer/data/scratch_sample.csv',
                       low_memory=False).drop(columns=['Unnamed: 0'])

    def test1(self):
        """column input is not a string"""
        with self.assertRaises(ValueError):
            data = self.data
            column = 4
            block_search = None
            search.search_data(data, column, block_search)

    def test2(self):
        """column input is not an option"""
        with self.assertRaises(ValueError):
            data = self.data
            column = 'Number'
            block_search = None
            search.search_data(data, column, block_search)

    def test3(self):
        """not all blocks are block types"""
        with self.assertRaises(ValueError):
            data = self.data
            column = 'block-type'
            block_search = ['&', 'not-a-block']
            search.search_data(data, column, block_search)

    def test4(self):
        """not all blocks are strings"""
        with self.assertRaises(ValueError):
            data = self.data
            column = 'block-type'
            block_search = [51, 31, 23]
            search.search_data(data, column, block_search)

    def test5(self):
        """No block types to search by"""
        with self.assertRaises(ValueError):
            data = self.data
            column = 'block-type'
            block_search = []
            search.search_data(data, column, block_search)

    def test6(self):
        """One shot test: only search for 1 block type"""
        data = self.data
        column = 'block-type'
        block_search = ['&']
        result = search.search_data(data, column, block_search)
        self.assertEqual(result.iloc[0].p_ID, 99457867)

    def test7(self):
        """One shot test: search for 2 block, already been searched"""
        data = self.data
        column = 'block-type'
        block_search = ['&', '+']
        block_search_sum = sum([data[block] for block in block_search])
        data.insert(len(data.columns), 'search_sum', block_search_sum)
        result = search.search_data(data, column, block_search)
        self.assertEqual(result.iloc[0].p_ID, 98955356)

    def test8(self):
        """One shot test: search for a column"""
        data = self.data
        column = 'Mastery'
        block_search = None
        result = search.search_data(data, column, block_search)
        self.assertEqual(result.iloc[0].p_ID, 98578463)


if __name__ == '__main__':
    unittest.main()
