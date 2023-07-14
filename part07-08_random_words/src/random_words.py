# Write your solution here
from random import sample
def words(n: int, beginning: str):
    lst = []
    with open("words.txt","r") as f:
        for lines in f:
            lines = lines.replace("\n","")
            if beginning == lines[:len(beginning)]:
                lst.append(lines)
    return sample(lst, n)

#OFFICIAL SOLUTION:
# import random
# def words(n: int, beginning: str):
#     word_list = []
#     with open("words.txt") as file:
#         for word in file:
#             word = word.replace("\n","")
#             if word.startswith(beginning):
#                 word_list.append(word)
#     if len(word_list) < n:
#         raise ValueError("Not enough suitable words can be found!")
#     return random.sample(word_list, n)