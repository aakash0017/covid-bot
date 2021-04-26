import numpy as np


# load files from data directory
def load_file(file_path):
    return np.load(file_path, allow_pickle=True)