import os
import unittest
import pandas as pd
import numpy as np
from scratch_explorer import model_fit

"""
A series of unit tests for the RandomForest Regression module
"""


class test_rf_regression(unittest.TestCase):
    
    def setUp(self):
        # getting paths to data file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'data/scratch_sample.csv')

        self.data_modeling = pd.read_csv(filename)

    def test_fit_model(self):
        """
        Tests model object, feature list, and diagnostics created
        """

        self.data = self.data_modeling
        model, feature_list, diagnostics = model_fit.fit_model(self.data)

        self.assertIsInstance(model, 'sklearn.multioutput.MultiOutputRegressor', 
        'model object not multi output regressor')
        
        self.assertTrue(feature_list, 'feature list not created')

        self.assertTrue(diagnostics, 'diagnostics not created')
            
    def test_file_export(self):
        """
        Test that module writes files
        """
        dirname = os.path.dirname(__file__)
        filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
        filename_features = os.path.join(dirname, 'exports/feature_list.sav')
        filename_diagnostics = os.path.join(dirname, 'exports/diagnostics.sav')
        
        self.assertTrue(os.path.isfile(filename_model),
        'model object not written to disk')
        #check that model exists

        self.assertTrue(os.path.isfile(filename_features),
        'features list not written to disk')
        #check that features list exist

        self.assertTrue(os.path.isfile(filename_diagnostics),
        'model diagnostics not written to disk')
        #check that diagnostics file exists
