import pandas as pd
import numpy as np

#replacing dashes with underscores
dat.columns = [i.replace('-', '_') for i in dat.columns]

#removing redundant columns
dat = dat.drop(columns=['Script_ID','p_ID'])

#remove unnecessary columns
dat = dat[dat.columns[~dat.columns.str.contains('param')]]