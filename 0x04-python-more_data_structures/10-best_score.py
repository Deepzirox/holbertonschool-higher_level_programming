#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_score = max(a_dictionary.values())
        keys = a_dictionary.keys()
        for key in keys:
            if a_dictionary[key] == max_score:
                return key
    return None