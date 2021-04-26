import numpy as np

# load files from data directory
def load_file(file_path):
    return np.load(file_path, allow_pickle=True)

# update resource dict
def update_dict(res_dict, update_key):
    for key, value in res_dict.items():
        if key == update_key:
            res_dict[key] = 1
    return res_dict 

def example():
    list_ = list(load_file('data/res.npy'))
    dict_ = dict(zip(list_, [0]*len(list_)))
    return update_dict(dict_, 'Oximeter')

# print(example())