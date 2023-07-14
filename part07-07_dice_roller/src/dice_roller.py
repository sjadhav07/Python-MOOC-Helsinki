# Write your solution here
from random import choice

def roll(die: str):
    diea = [3, 3, 3, 3, 3, 6]
    dieb = [2, 2, 2, 5, 5, 5]
    diec = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return choice(diea)
    elif die == "B":
        return choice(dieb)
    elif die == "C":
        return choice(diec)

def play(die1: str, die2: str, times: int):
    a = 0
    b = 0
    c = 0
    for i in range(times):
        win1 = roll(die1)
        win2 = roll(die2)
        if win1 > win2:
            a += 1
        elif win1 < win2:
            b += 1
        elif win1 == win2:
            c += 1
    return (a, b, c)

#OFFICIAL SOLUTION:
# from random import sample
# def roll(die: str):
#     dices = {
#         "A": [3, 3, 3, 3, 3, 6],
#         "B": [2, 2, 2, 5, 5, 5],
#         "C": [1, 4, 4, 4, 4, 4]
#     }
 
#     return sample(dices[die], 1)[0]
 
# def play(die1: str, die2: str, times: int):
#     v1 = 0
#     v2 = 0
#     t = 0
#     for i in range(times):
#         n1 = roll(die1)
#         n2 = roll(die2)
#         if n1>n2:
#             v1 += 1
#         elif n1<n2:
#             v2 += 1
#         else:
#             t += 1
#     return v1, v2, t
