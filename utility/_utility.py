import numpy as np
import enchant
import sys
sys.path.append('../')
from data.default_dict import default_dict
from data.res_list import needhelp_Reslist, needhelp_Reslist_op
import re


def take_input(user_input, input_type):
    user_input = user_input.lower()
    # handle input_type = 'int'
    processed_input = check_validity(user_input, input_type)
    return processed_input

def check_validity(user_input, input_type):

    sim_input, status = most_similar(user_input, input_type)
    if status == True:
        # possible_inputs = handle_invalid_input(user_input, input_type)
        return [status, '']
    else:
        return sim_input

# universal invalid user input handler

def handle_invalid_input(user_input, input_type):
    k = 5
    if input_type == 'city':
        objective = load_cities()
    elif input_type == 'res':
        objective = load_resources()
    elif input_type == 'state':
        objective = load_states()
    scores = []
    # calculate distance for all cities
    for content in objective:
        distance = enchant.utils.levenshtein(user_input, content)
        scores.append(distance)
    # convert to numpy array
    scores = np.array(scores)
    possible_inputs = objective[np.argpartition(scores, k)[:k]]
    return list(possible_inputs)

# universal similarity checker for both city and resource input type

def most_similar(user_input, input_type):
    if input_type == 'city':
        objective = load_cities()
    elif input_type == 'res':
        objective = load_resources()
    elif input_type == 'state':
        objective = load_states()
    status = False
    scores = []
    # calculate score b/w contents in objective list and user_input
    for content in objective:
        distance = enchant.utils.levenshtein(user_input, content)
        scores.append(distance)
    # convert to numpy array
    scores = np.array(scores)
    min_idx = scores.argmin()
    if scores[min_idx] > 3:
        status = True
    sim_obj = objective[min_idx]
    return sim_obj, status


def load_cities():
    return np.load('data/cities.npy', allow_pickle=True)

def load_resources():
    return np.load('data/res.npy', allow_pickle=True)

def load_states():
    return np.load('data/states.npy', allow_pickle=True)

# load resources and apply mapping from idx -> resource names
def idx_2_res():
    res = load_resources()
    idx_2_res = dict()
    for idx, res in enumerate(res):
        idx_2_res[idx] = res
    return idx_2_res

# split input resources into list
def res_spliter(inp_res):
    res = inp_res.split(' ')
    return res

def read_user_input(user_input):

    l = user_input.split('\n')
    name = l[0]
    mobile = l[1]
    email = l[2]
    city = l[3]
    state = l[4]
    resources = l[5]
    description = l[6]

    return name, email, mobile, city, state, resources, description

def generate_dict(detail_list):
    dict_ = default_dict()
    for idx, i in enumerate(dict_):
        dict_[i] = detail_list[idx]
    return dict_

def array2dict(array):
    return dict(enumerate(array.flatten(), 1))

def send_resource_message():
    tmp_string = ""
    for key, value in idx_2_res().items():
        tmp_string = tmp_string + "{0:<10} {1}".format(key, value) + "\n"

    result = """Resource List: \n{} """.format(tmp_string)
    return result

def regex_checker(recived_txt):
    # type_check values for contributor: 1, needhelp: 2, otherwise: 3
    # TODO add try and catch block when dealing with multiple type checks
    regex = r"^([a-zA-Z]+(\\n[a-zA-Z]+)+)([0-9]*)@[a-zA-Z]+\.([a-zA-Z]+(\\[a-zA-Z]+)+)[0-9]+\\n([a-zA-Z]+(\\n[a-zA-Z]+)+)\\n([0-9]+( [0-9]+)*)\\n[a-zA-Z].*$"
    refined_txt = recived_txt.replace("\n", "\\n")
    matches = re.match(regex, refined_txt)
    if matches:
        return "1"
    else:
        regex = r"^[0-9]+\sin\s[a-zA-Z]+$"
        matches = re.match(regex, recived_txt)
        if matches:
            return "2"
        else:
            regex = r"^[a-zA-Z]{1,2}(\+|\-)+( [a-zA-Z]{1,2}(\+|\-))*.*$"
            matches = re.match(regex, recived_txt)
            if matches:
                return "1"
            else:
                pass
    return "3"


def process_needhelp_input(user_input):
    # split needhelp input into resource id and city
    split_list = user_input.split('in')
    result_list = [elements.strip() for elements in split_list]
    return result_list[0], result_list[1]

# For flask app for sending instant message on call of /needhelp
def decode_residx():
    res_list = needhelp_Reslist()
    dict_ = dict()
    for idx, res in enumerate(res_list):
        dict_[idx] = res
    return dict_

# For internal operational basis where blood grp are concatenated to _ with plasma
def decode_residx_op():
    res_list = needhelp_Reslist_op()
    dict_ = dict()
    for idx, res in enumerate(res_list):
        dict_[idx] = res
    return dict_

# for sending meesage on as a post request under /needhelp block
def send_needhelp_reslist_msg():
    tmp_string = ""
    for key, value in decode_residx().items():
        tmp_string = tmp_string + "{0:<15} {1}".format(key, value) + "\n"

    result = """Resource List: \n{} """.format(tmp_string)
    return result

# Factoring getRequest Result.
def process_needhelp_result(get_Result_list):
    # convert the get_Request list to extract name and mobile only.
    # temp_list = []
    temp_list = [[i[0].lower(), i[3]] for i in get_Result_list]
    # main sorted list 
    result_list = list(set(map(lambda i: tuple(sorted(i)), temp_list)))
    return result_list

def needhelp_message(result_list):
    temp_string = ""
    for tup in result_list:
        temp_string = temp_string + "{0:<5} {1}".format(tup[1], tup[0]) + "\n"
    result_message = """Here are some contacts for requested covid resource:  \n{} """.format(temp_string)
    return result_message

