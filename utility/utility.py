import wordSimilarity
import numpy as np

def handle_invalid_input(user_input, input_type):
    cities_list = np.load('../data/cities.npy', allow_pickle=True)
    possible_input = []
    if input_type == 'string':
        possible_input = [i.lower() for i in cities_list if user_input[0] == i[0].lower()]
        return possible_input
    else:
        return 'please enter a valid input'
    
def check_validity(user_input, input_type):
    
    if input_type == 'string':
        user_input_status = wordSimilarity.check_city_similarity(user_input)
    if input_type == 'int':
        user_input_status = check_integer_input(user_input)
    if user_input_status == 'invalid':
        user_input = handle_invalid_input(user_input, input_type)
        status = 'invalid'
        return [status,user_input]
    else:
        user_input = wordSimilarity.check_city_similarity(user_input)
        return user_input


def take_input(input_type):
    # user_input = input("")
    user_input = 'Jaipur'
    if input_type == 'string':
        user_input = user_input.lower()
    processed_input = check_validity(user_input, input_type)
    return processed_input

def check_integer_input(user_input):
    return user_input
    

def example_main():
    processed_input = take_input('string')
    return processed_input
    
print(example_main())



    