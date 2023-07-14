# Write your solution here
def no_shouting(lst: list):
    new_list = []
    for word in lst:
        if word.isupper() == False:
            new_list.append(word)
    return new_list