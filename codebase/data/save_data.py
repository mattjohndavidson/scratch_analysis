"""
This module collects the scratch data from a locally saved copy of the data
from https://drive.google.com/drive/folders/12L-ot-zOde35hViINe9wzTl9DkVTtDCs
(collected by TUDelft). Using the files code.csv and metadata.csv, this module
parses the data needed to run scratch_analysis and saves it as scratch_data.csv
in the data folder. The user does not need to run this module.
"""
import os.path as op
import pandas as pd
import numpy as np


def save_data():
    """
    Creates scratch_data.csv
    """
    local_path_meta = '/Users/jacobcohen/Downloads/metadata.csv' #(31.2 MB)
    local_path_code = '/Users/jacobcohen/Downloads/code.csv' #(3.76 GB)
    file_out_path = 'scratch_data.csv'

    df = pd.read_csv(local_path_code)
    metadata = pd.read_csv(local_path_meta)

    projects = df.groupby('p_ID')['block-type'].value_counts().unstack(fill_value=0).reset_index()
    projects.columns.name = None

    total_blocks = df.groupby('p_ID')['total-blocks'].first()
    projects.insert(1, 'total-blocks',total_blocks.reset_index()['total-blocks'])

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
                        'is-remix','Abstraction','Parallelism',
                        'Logic', 'Synchronization', 'FlowControl',
                        'UserInteractivity', 'DataRepresentation',
                        'Mastery', 'Clones','CustomBlocks']

    merged = metadata[metadata_columns].merge(right=projects[projects_columns],
                                              how='inner', on='p_ID')
    merged.to_csv(file_out_path)


if __name__== "__main__":
    save_data()