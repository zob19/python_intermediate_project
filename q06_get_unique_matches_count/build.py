# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array=read_ipl_data_csv('data/ipl_matches_small.csv','|S25')
    unique = np.unique(ipl_matches_array[:,0])
    return len(unique)

