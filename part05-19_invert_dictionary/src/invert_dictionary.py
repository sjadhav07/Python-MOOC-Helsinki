# Write your solution here

def invert(dictionary: dict):
    new_dictionary = {y: x for x, y in dictionary.items()}
    dictionary.clear()
    for key, value in new_dictionary.items():
        dictionary[key] = value


