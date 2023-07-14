# Write your solution here
from random import choice, randint, shuffle
from string import ascii_lowercase
def generate_strong_password(length: int, a = False, b = False):
    passwd = ""
    if length > 1:
        num1 = randint(1, length-1)
    if length > 2:
        num2 = randint(1, length-2)
        num3 = length-num2-1
    if a == False and b == False:
        for i in range(length):
            passwd += choice(ascii_lowercase)
    elif a == True and b == False:
        for i in range(num1):
            passwd += choice(ascii_lowercase)
        for i in range(length-num1):
            passwd += choice("0123456789")
    elif a == True and b == True:
        for i in range(num2):
            passwd += choice(ascii_lowercase)
        for i in range(num3):
            passwd += choice("0123456789")
        for i in range(length-num2-num3):
            passwd += choice("!?=+-()#")
    else:
        for i in range(num1):
            passwd += choice(ascii_lowercase)
        for i in range(length-num1):
            passwd += choice("!?=+-()#")
    lst = []
    for letter in passwd:
        lst.append(letter)
    shuffle(lst)
    return ''.join(lst)

#OFFICIAL SOLUTION:
# from random import choice, randint
# from string import ascii_lowercase, digits
 
# def generate_strong_password(length: int, numbers: bool, special_characters: bool):
#     special_chars = "!?=+-()#"
#     # One letter at beginning of the password
#     passwd = choice(ascii_lowercase)
#     choice_set = ascii_lowercase
 
#     # If numbers is wanted, add at least one number
#     if numbers:
#         passwd = add_character(passwd, digits)
#         choice_set += digits
 
#     # same for special characters
#     if special_characters:
#         passwd = add_character(passwd, special_chars)
#         choice_set += special_chars
 
#     # build the rest of the password from the whole set
#     while (len(passwd) < length):
#         passwd = add_character(passwd, choice_set)
 
#     return passwd
 
# # Add a random character from the given set either
# # at the beginning or end of the string
# def add_character(passwd: str, characters):
#     character = choice(characters)
#     if randint(1,2) == 1:
#         return character + passwd
#     else:
#         return passwd + character
