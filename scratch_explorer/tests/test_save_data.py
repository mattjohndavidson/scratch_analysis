import unittest
import pandas as pd
import numpy as np
from scratch_explorer import save_data

class test_save_data(unittest.TestCase):
    """Includes unit tests for save_data.py"""
    
    def test1(self):
        """Input is not a csv file"""
        with self.assertRaises(ValueError):
            save_data.save_data('metadata', 'code', 'ouput')


if __name__ == '__main__':
    unittest.main()