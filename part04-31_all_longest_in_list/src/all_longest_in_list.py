# Write your solution here
def all_the_longest(my_list):
    longest = len(my_list[0])
    for word in my_list:
        if len(word) > longest:
            longest = len(word)
    lst = []
    for word in my_list:
        if len(word) == longest:
            lst.append(word)
    return lst