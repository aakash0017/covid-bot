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

def plasma_handler(res_dict, blood_grps, user_input):
    grps = user_input.split(' ')
    print(grps)
    for bg in grps:
        if res_dict['Plasma'] == 1:
            blood_grps.append(bg.lower())
    return blood_grps

def check_plasma(res_list):
    if 'Plasma' in res_list:
        return True
    else:
        return False

def user_res(res_dict):
    return [key for key, val in res_dict.items() if val == 1]

def concat_grps(res_list, blood_grps):
    # remove plasma
    res_list.remove('Plasma')
    string = 'Plasma_{0}'
    # concat blood grps to string 
    return [res_list.append(string.format(bg)) for bg in blood_grps]

def example():
    list_ = list(load_file('../data/res.npy'))
    dict_ = dict(zip(list_, [0]*len(list_)))
    update_dict(dict_, 'Plasma')
    return plasma_handler(dict_, 'AB')

# list_ = list(load_file('../data/res.npy'))
# dict_ = dict(zip(list_, [0]*len(list_)))
# dict_['Plasma'] = 1
# dict_['Oximeter'] = 1
# print(type(user_res(dict_)))

# print(concat_grps(['Plasma', 'Oximeter'], ['ab+ve', 'b+ve']))