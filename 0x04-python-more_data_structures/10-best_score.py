#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    max_score = max(a_dictionary.values())
    keys = a_dictionary.keys()
    for key in keys:
        if a_dictionary[key] == max_score:
            return key


a_dictionary = {}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))