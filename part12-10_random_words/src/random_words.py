# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
        return ((char for char in characters for i in range(length)) for j in range(amount))

#OFFICIAL SOLUTION:
# from random import choice
 
# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))