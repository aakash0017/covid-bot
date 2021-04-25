
import enchant
import numpy as np


def check_city_similarity(word):

    cities_list = np.load('../data/cities.npy', allow_pickle=True)
    most_similar = []
    for i in cities_list:
        if enchant.utils.levenshtein(word.lower(), i) < 4:
            most_similar.append(i)
    if len(most_similar) == 0:
        return 'invalid'
    return most_similar[0].lower()
