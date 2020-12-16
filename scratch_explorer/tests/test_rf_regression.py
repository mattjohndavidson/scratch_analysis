import os
import unittest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
from scratch_explorer import model_fit

"""
A series of unit tests for the RandomForest Regression module
"""


class test_rf_regression(unittest.TestCase):
    
    def setUp(self):
        # getting paths to data file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname,'..','data/scratch_sample.csv')

        self.data_modeling = pd.read_csv(filename)

    def test_fit_model(self):
        """
        Tests model object, feature list, and diagnostics created
        """

        self.data = self.data_modeling
        model, feature_list, diagnostics = model_fit.fit_model(self.data)

        self.assertTrue(model, 'model not created')
        
        self.assertTrue(feature_list, 'feature list not created')

        self.assertTrue(diagnostics, 'diagnostics not created')
            
    def test_file_export(self):
        """
        Test that export module is called

        Checks that inputs were correct
        """

        with patch('scratch_explorer.model_fit.export_files') as export_call, \
            patch('scratch_explorer.model_fit.fit_model') as fit_call:
            fit_call.return_value = ['model', 'feature_list', 'diagnostics']
            model_fit.main()
            export_call.assert_called_once_with('model', 'feature_list', 'diagnostics')
