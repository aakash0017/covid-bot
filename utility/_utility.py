import numpy as np
import enchant

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
    res = list(load_resources())
    idx_2_res = dict()
    for idx, res in enumerate(res):
        idx_2_res[idx] = res
    return idx_2_res

# split input resources into list
def res_spliter(inp_res):
    res = inp_res.split(' ')
    return res


# res_id = 1
# idx_2_res_map = idx_2_res()
# for i, i1 in idx_2_res_map.items():
#     print(i, i1)

# Lambda = lambda x: idx_2_res_map[int(x)]
# X = res_spliter('1 2 3')
# resources = [Lambda(x) for x in X]

def read_user_input(user_input):

    l = user_input.split('\n')
    name = l[0]
    email = l[1]
    mobile = l[2]
    city = l[3]
    state = l[4]
    resources = l[5]
    description = l[6]

    return name, email, mobile, city, state, resources, description

# sample_input = 'aakash bhatnagar\nakashbharat.bhatnagar@gmail.com\n8384041898\nvaodara\ndelhi\nplasma AB+\ndescription'
# print(read_user_input(sample_input))

print(check_validity('wdadwqe', 'city'))
