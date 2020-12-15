import os
import unittest
import pandas as pd
import numpy as np
from codebase import model_fit

"""
A series of unit tests for the RandomForest Regression module
"""

# getting paths to data file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/project_db_1000.csv')

class test_rf_regression(unittest.TestCase):
    
    def setUp(Self):
        self.data_raw = read_data()
        self.data_clean = clean_data(data_raw)
        self.data_modeling = flatten_data(data_clean)

    def test_fit_model(Self):
        """
        Tests that features are successfully created and
        test/train/split successful
        """
        with self.assertEqual(train_features.shape[0], train_labels.shape[0],
        'training features and labels have different number of rows')
            data = data_modeling
            model_fit.prepare_data(data)
        
        with self.assertEqual(test_features.shape[0], test_labels.shape[0],
        'testing features and labels have different number of rows')
            data = data_modeling
            model_fit.prepare_data(data)
        
        with self.assertEqual(test_labels.shape[1], train_labels.shape[1],
        'testing and training labels have different number of columns')
            data = data_modeling
            model_fit.prepare_data(data)

        with self.assertEqual(test_features.shape[1], train_features.shape[1],
        'testing and training features have different number of columns')
            data = data_modeling
            model_fit.prepare_data(data)


            #check for model object instantiation, of the correct type
        # RF regresssion + multioutput
    
        #ensure that diagnostics not empty

    def test_file_export(Self):
        """
        Test that module writes files
        """
        dirname = os.path.dirname(__file__)
        filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
        filename_features = os.path.join(dirname, 'exports/feature_list.sav')
        filename_diagnostics = os.path.join(dirname, 'exports/diagnostics.sav')
        
        with self.assertTrue(os.path.isfile(filename_model))
        #check that model exists

        with self.assertTrue(os.path.isfile(filename_features))
        #check that features list exist

        with self.assertTrue(os.path.isfile(filename_diagnostics))
        #check that diagnostics file exists
