import numpy as np
import re

# load files from data directory
def load_file(file_path):
    return np.load(file_path, allow_pickle=True)

# update resource dict
def update_dict(res_dict, update_key):
    for key, value in res_dict.items():
        if key == update_key:
            res_dict[key] = 1
    return res_dict 

def validate_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False

def validate_mobile(mobile):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if (Pattern.match(mobile)):
        return True   
    else :
        return False

def plasma_handler(res_dict, blood_group):
    if res_dict['Plasma'] == 1:
        res_dict['blood_grp'] = blood_group.lower()
    return res_dict

def check_plasma(res_list):
    if 'Plasma' in res_list:
        return True
    else:
        return False

# def Factor_Resources(res_dict):
#     for key, value in res_dict.items():
#         if value

def example():
    list_ = list(load_file('data/res.npy'))
    dict_ = dict(zip(list_, [0]*len(list_)))
    update_dict(dict_, 'Plasma')
    return plasma_handler(dict_, 'AB')
