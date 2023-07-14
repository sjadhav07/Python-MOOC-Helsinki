# Write your solution here
from multiprocessing import reduction


def everything_reversed(lst):
    new_list = []
    for word in lst[::-1]:
        new_list.append(word[::-1])
    return new_list


