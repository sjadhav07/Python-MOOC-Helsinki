# Write your solution here
from random import sample
from string import ascii_lowercase
def generate_password(length: int):    
    return ''.join(sample(ascii_lowercase, length))


#OFFICIAL SOLUTION:
# from random import choice
# from string import ascii_lowercase
# def generate_password(length: int):
#     passwd = ""
#     for i in range(length):
#         passwd += choice(ascii_lowercase)
#     return passwd