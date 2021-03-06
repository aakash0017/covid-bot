import numpy as np
import re
from cms_queries.queries import post_request

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

# def plasma_handler(res_dict, blood_grps, user_input):
#     grps = user_input.split(' ')
#     for bg in grps:
#         if res_dict['Plasma'] == 1:
#             blood_grps.append(bg.lower())
#     return blood_grps

def plasma_handler(res_dict, blood_grps, user_input):
    grps = user_input.split(' ')
    for bg in grps:
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
    # res_list.remove('Plasma')
    string = 'Plasma_{0}'
    # concat blood grps to string 
    return [res_list.append(string.format(bg)) for bg in blood_grps]

def save_details(details_dict, chat_id, hasplasma_Flag):
    details_dict['chat_id'] = chat_id
    details_dict['has_plasma'] = hasplasma_Flag
    details_dict['Resources'].remove("Plasma")
    tmp_string = ''
    for i in details_dict['Resources']:
        tmp_string += i + ','
    details_dict['Resources'] = tmp_string
    print("67", details_dict)
    dict_body = def_dict_2_post_mapping(details_dict)
    url = 'https://covid-bot-cms.herokuapp.com'
    res = post_request(endpoint='/Beta-objects', body=dict_body, url=url)
    print(res)
    return res
    
def save_details_app(details_dict, chat_id, hasplasma_Flag):
    details_dict['chat_id'] = chat_id
    details_dict['has_plasma'] = hasplasma_Flag
    print("67", details_dict)
    dict_body = def_dict_2_post_mapping(details_dict)
    url = 'https://covid-bot-cms.herokuapp.com'
    res = post_request(endpoint='/Beta-objects', body=dict_body, url=url)
    print(res)
    return res
    
    
def after_bg_save(details_dict, chat_id, hasplasma_Flag=False):
    details_dict['chat_id'] = chat_id
    details_dict['has_plasma'] = hasplasma_Flag
    
    tmp_string = ''
    for i in details_dict['Resources']:
        tmp_string += i + ','
    details_dict['Resources'] = tmp_string
    print("60", details_dict)
    
    dict_body = def_dict_2_post_mapping(details_dict)
    url = 'https://covid-bot-cms.herokuapp.com'
    res = post_request(endpoint='/Beta-objects', body=dict_body, url=url)
    print(res)
    return res
    
def def_dict_2_post_mapping(details_dict):
    dict_ = {'name': '', 'mobile': '', 'email': '', 'city': '', 'state': '', 'resources': '', 'description': '', 'chatID': '', 'hasPlasma': ''}
    dict_['name'] = details_dict['Name']
    dict_['mobile'] = details_dict['Mobile']
    dict_['email'] = details_dict['Email']
    dict_['city'] = details_dict['City']
    dict_['state'] = details_dict['State']
    dict_['resources'] = details_dict['Resources']
    dict_['description'] = details_dict['Description']
    dict_['chatID'] = details_dict['chat_id']
    dict_['hasPlasma'] = details_dict['has_plasma']
    return dict_