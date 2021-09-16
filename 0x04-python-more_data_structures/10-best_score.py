#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = -1
    favourite = None
    for key in a_dictionary:
        if max_score < a_dictionary[key]:
            max_score = a_dictionary[key]
            favourite = key
    return favourite
