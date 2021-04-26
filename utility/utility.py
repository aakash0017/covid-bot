from data.resource_dict import resource_dict
import numpy as np
import enchant
import numpy as np
import sys
sys.path.append('../')


def handle_invalid_input(user_input, input_type):
    cities_list = np.load('../data/cities.npy', allow_pickle=True)
    resource_list = np.load('../data/res.npy', allow_pickle=True)
    possible_input = []
    if input_type == 'city':
        possible_input = [i.lower()
                          for i in cities_list if user_input[0] == i[0].lower()]
        return possible_input

    elif input_type == 'resources':
        possible_input = [i.lower()
                          for i in resource_list if user_input[0] == i[0].lower()]
        return possible_input
    else:
        return 'please enter a valid input'


def check_validity(user_input, input_type):

    if input_type == 'int':
        if check_integer_input(user_input) != 'invalid':
            return user_input
    else:
        user_input_status = check_similarity(user_input, input_type)

    if user_input_status == 'invalid':
        user_input = handle_invalid_input(user_input, input_type)
        status = 'invalid'
        return [status, user_input]
    else:
        user_input = check_similarity(user_input, input_type)
        return user_input


def take_input(input_type):
    # user_input = input("")
    user_input = 'jaipur'
    if input_type == 'city':
        user_input = user_input.lower()
    else:
        user_input = int(user_input)

    processed_input = check_validity(user_input, input_type)
    return processed_input

def check_integer_input(user_input):
    return user_input


def example_main():
    processed_input = take_input('city')
    return processed_input


def check_similarity(user_input, type_input):
    resource_list = resource_dict()
    cities_list = np.load('../data/cities.npy', allow_pickle=True)

    if type_input == 'city':
        most_similar = []
        for i in cities_list:
            if enchant.utils.levenshtein(user_input.lower(), i) < 4:
                most_similar.append(i)
        if len(most_similar) == 0:
            return 'invalid'
        return most_similar[0].lower()

    if type_input == 'resources':
        most_similar = []
        for i in resource_list:
            if enchant.utils.levenshtein(user_input.lower(), resource_list[i]) < 4:
                most_similar.append(i)
        if len(most_similar) == 0:
            return 'invalid'
        return most_similar[0].lower()


print(example_main())
