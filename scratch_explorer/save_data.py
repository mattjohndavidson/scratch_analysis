"""
This module collects the scratch data from a locally saved copy of the data
from https://drive.google.com/drive/folders/12L-ot-zOde35hViINe9wzTl9DkVTtDCs
(collected by TUDelft). Using the files code.csv and metadata.csv, this module
parses the data needed to run scratch_analysis and saves it as scratch_data.csv
in the data folder. The user does not need to run this module.
"""
import sys
import errno
import os
import os.path as op
import pandas as pd
import numpy as np


def get_data(local_path_meta, local_path_code):
    """
    Creates scratch_data.csv

    Params
    ------
        local_path_meta: csv file path where metadata.csv is saved
        local_path_code: csv file path where code.csv is saved

    Returns
    -------
        merged: pandas DataFrame to be used with scratch_explorer
    """
    paths = [local_path_meta, local_path_code]
    if not all(path.endswith('.csv') for path in paths):
        raise ValueError('Files must be csv files.')

    URL = 'https://drive.google.com/drive/folders/12L-ot-zOde35hViINe9wzTl9DkVTtDCs'
    if not op.exists(local_path_meta):
        e_message = 'Download metadata.csv from\n{}\n'.format(URL) \
                    + os.strerror(errno.ENOENT)
        raise FileNotFoundError(errno.ENOENT, e_message, local_path_meta)
    if not op.exists(local_path_code):
        e_message = 'Download code.csv from\n{}\n'.format(URL) \
                    + os.strerror(errno.ENOENT)
        raise FileNotFoundError(errno.ENOENT, e_message, local_path_code)

    df = pd.read_csv(local_path_code)
    metadata = pd.read_csv(local_path_meta)

    projects = df.groupby('p_ID')['block-type'].value_counts().unstack(fill_value=0).reset_index()
    projects.columns.name = None

    total_blocks = df.groupby('p_ID')['total-blocks'].first()
    projects.insert(1, 'total-blocks',
                    total_blocks.reset_index()['total-blocks'])

    # Keep only blocks used in more than 100,000 projects, top 63 blocks
    blocks_data = df[['p_ID', 'block-type']]
    counts = blocks_data.groupby('block-type').count().p_ID.rename('counts')
    counts_sorted = counts.sort_values(ascending=False)
    TOP = 63

    projects_columns = np.insert(counts_sorted[0:TOP].index.values,
                                 0, ['p_ID', 'total-blocks'])
    metadata_columns = ['p_ID', 'project-name', 'username',
                        'total-views', 'total-remixes',
                        'total-favorites', 'total-loves',
                        'is-remix', 'Abstraction', 'Parallelism',
                        'Logic', 'Synchronization', 'FlowControl',
                        'UserInteractivity', 'DataRepresentation',
                        'Mastery', 'Clones', 'CustomBlocks']

    merged = metadata[metadata_columns].merge(right=projects[projects_columns],
                                              how='inner', on='p_ID')
    return merged


def main():
    """Runs get_data() and saves to user-defined location.

    My example usage:
        python save_data.py /Users/jacobcohen/Downloads/metadata.csv \
        /Users/jacobcohen/Downloads/code.csv data/scratch_data.csv
    """
    if not len(sys.argv) == 4:
        sys.exit('Usage: python save_data.py <metadata.csv path> \
                  <code.csv path> <scratch_data.csv path>')
    else:
        local_path_meta = sys.argv[1]
        local_path_code = sys.argv[2]
        file_out_path = sys.argv[3]
        paths = [local_path_meta, local_path_code, file_out_path]
        if not all(path.endswith('.csv') for path in paths):
            raise ValueError('All paths must be csv file paths.')
        if op.exists(file_out_path):
            need_input = True
            while need_input:
                ans = input('File {} already exists. Do you want to overwrite (y/n)?'.format(file_out_path))
                if ans == 'n':
                    need_input = False
                    sys.exit(0)
                elif ans == 'y':
                    need_input = False
                else:
                    pass

        to_save = get_data(local_path_meta, local_path_code)
        to_save.to_csv(file_out_path)


if __name__ == "__main__":
    main()
