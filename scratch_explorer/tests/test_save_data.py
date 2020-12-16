import unittest
from unittest.mock import Mock, patch
import pandas as pd
import numpy as np
from scratch_explorer import save_data

class test_save_data(unittest.TestCase):
    """Includes unit tests for save_data.py"""
    @classmethod
    def setUpClass(cls):
        """Make 2 dataframes to mock the code and the metadata"""
        np.random.seed(0)
        test_n = 10
        p_ids = np.random.randint(low=10000001, high=99999999, size=test_n)
        p_ids_long = np.repeat(p_ids, np.random.randint(low=7, high=16, size=test_n))

        test_n_blocks = len(p_ids_long)
        sprite_types = np.random.randint(low=1, high=100, size=test_n_blocks)
        total_blocks = np.random.randint(low=1, high=100, size=test_n_blocks)
        block_types_ints = np.random.randint(low=10000, high=99999, size=test_n_blocks)
        block_types = [str(block) for block in block_types_ints]

        cls.ex_code = pd.DataFrame({'p_ID': p_ids_long,
                                    'sprite-type': sprite_types,
                                    'total-blocks': total_blocks,
                                    'block-type': block_types})

        p_ID = p_ids
        project_name = [str(name) for name in np.random.randint(low=10000,
                                                                 high=99999,
                                                                 size=test_n)]
        username = [str(name) for name in np.random.randint(low=1000,
                                                                 high=9999,
                                                                 size=test_n)]
        total_views = np.random.randint(low=100, high=999, size=test_n)
        total_remixes = np.random.randint(low=100, high=999, size=test_n)
        total_favorites = np.random.randint(low=100, high=999, size=test_n)
        total_loves = np.random.randint(low=100, high=999, size=test_n)
        is_remix = np.random.randint(low=0, high=1, size=test_n)
        Abstraction = np.random.randint(low=0, high=3, size=test_n)
        Parallelism = np.random.randint(low=0, high=3, size=test_n)
        Logic = np.random.randint(low=0, high=3, size=test_n)
        Synchronization = np.random.randint(low=0, high=3, size=test_n)
        FlowControl = np.random.randint(low=0, high=3, size=test_n)
        UserInteractivity = np.random.randint(low=0, high=3, size=test_n)
        DataRepresentation = np.random.randint(low=0, high=3, size=test_n)
        Mastery = np.random.randint(low=0, high=3, size=test_n)
        Clones = np.random.randint(low=0, high=20, size=test_n)
        CustomBlocks = np.random.randint(low=0, high=20, size=test_n)

        cls.ex_meta = pd.DataFrame({'p_ID': p_ID,
                                    'project-name': project_name,
                                    'username': username,
                                    'total-views': total_views,
                                    'total-remixes': total_remixes,
                                    'total-favorites': total_favorites,
                                    'total-loves': total_loves,
                                    'is-remix': is_remix,
                                    'Abstraction': Abstraction,
                                    'Parallelism': Parallelism,
                                    'Logic': Logic,
                                    'Synchronization': Synchronization,
                                    'FlowControl': FlowControl,
                                    'UserInteractivity': UserInteractivity,
                                    'DataRepresentation': DataRepresentation,
                                    'Mastery': Mastery,
                                    'Clones': Clones,
                                    'CustomBlocks': CustomBlocks})


    def test_save1(self):
        """one input is not a csv file"""
        with self.assertRaises(ValueError):
            save_data.get_data('metadata.csv', 'code')


    @patch('os.path.exists')
    def test_save2(self, os_path_exists_mock):
        """metadata.csv does not exist"""
        with self.assertRaises(FileNotFoundError):
            os_path_exists_mock.side_effect = [False, True]
            save_data.get_data('metadata.csv', 'code.csv')
    
    
    @patch('os.path.exists')
    def test_save3(self, os_path_exists_mock):
        """code.csv does not exist"""
        with self.assertRaises(FileNotFoundError):
            os_path_exists_mock.side_effect = [True, False]
            save_data.get_data('metadata.csv', 'code.csv')


    @patch('pandas.read_csv')
    @patch('os.path.exists')
    def test_save4(self, os_path_exists_mock, read_csv_mock):
        """Smoke test of save_data()"""
        os_path_exists_mock.side_effect = [True, True]
        read_csv_mock.side_effect = [self.ex_code, self.ex_meta]
        result = save_data.get_data('metadata.csv', 'code.csv')


    def test_main1(self):
        """only 3 arguments are passed to save_data.py"""
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('sys.argv',
                                     ['save_data.py', 'metadata.csv',
                                      'code.csv']):
                save_data.main()


    def test_main2(self):
        """arguments passed to save_data.py are not csv files."""
        with self.assertRaises(ValueError):
            with unittest.mock.patch('sys.argv',
                                     ['save_data.py', 'metadata.csv',
                                      'code.csv','output']):
                save_data.main()


    @patch('builtins.input')
    @patch('os.path.exists')
    def test_main3(self, os_path_exists_mock, input_mock):
        """Output file already exists. Tests both responses."""
        os_path_exists_mock.side_effect = [True, True, False]
        input_mock.side_effect = ['d', 'n', 'y']
        with unittest.mock.patch('sys.argv',
                                 ['save_data.py', 'metadata.csv',
                                  'code.csv','output.csv']):
            with self.assertRaises(SystemExit):
                save_data.main()
            with patch('scratch_explorer.save_data.get_data') as get_data_call, \
                 patch('pandas.DataFrame.to_csv') as to_csv_call:
                get_data_call.return_value = pd.DataFrame()
                to_csv_call.side_effect = (lambda x: None)
                save_data.main()
                get_data_call.assert_called_once_with('metadata.csv', 'code.csv')
                to_csv_call.assert_called_once_with('output.csv')


if __name__ == '__main__':
    unittest.main()
