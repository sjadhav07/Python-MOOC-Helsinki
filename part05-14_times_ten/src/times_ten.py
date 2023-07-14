# Write your solution here
from tracemalloc import start


def times_ten(start_index: int, end_index: int):
    dict = {}
    num = start_index
    while num <= end_index:
        dict[num] = num*10
        num += 1
    return dict
