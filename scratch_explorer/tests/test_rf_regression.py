"""
A series of unit tests for the RandomForest Regression module
"""
import os
import unittest
import pandas as pd
from unittest.mock import MagicMock, patch
from scratch_explorer import model_fit


class test_rf_regression(unittest.TestCase):

    def setUp(self):
        # getting paths to data file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '..', 'data/scratch_sample.csv')

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

    @patch('joblib.dump')
    @patch('pandas.read_csv')
    @patch('numpy.c_')
    @patch('scratch_explorer.model_fit.fit_model')
    def test_file_export(self, fit_mock, npc_mock, read_csv_mock, dump_mock):
        """
        Test that export module is called

        Checks that inputs were correct
        """
        model = MagicMock()
        feature_list = MagicMock()
        npc_mock.return_value = MagicMock()
        read_csv_mock.return_value = ''
        fit_mock.return_value = [model, feature_list, 'diagnostics']
        dump_mock.side_effect = lambda x, y: None

        with patch('pandas.DataFrame') as df_mock:
            df_mock.return_value = MagicMock()
            model_fit.main()

        dump_mock.assert_called()
