# Write your solution here
import string

def change_case(orig_string: str):
    new_string = ""
    for letter in orig_string:
        if letter.islower():
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string

def split_in_half(orig_string: str):
    length = len(orig_string)//2
    return (orig_string[:length],orig_string[length:])

def remove_special_characters(orig_string: str):
    new_string = ""
    
    for char in orig_string:
        if char in string.ascii_letters+" " +string.digits:
            new_string += char
    return new_string

#OFFICIAL SOLUTION:
# from string import ascii_letters, digits
 
# def change_case(orig_string: str):
#     new_string = ""
#     for character in orig_string:
#         if character.isupper():
#             new_string += character.lower()
#         elif character.islower():
#             new_string += character.upper()
#         else:
#             new_string += character
 
#     return new_string
 
# def split_in_half(orig_string: str):
#     return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
 
# def remove_special_characters(orig_string: str):
#     allowed = ascii_letters + digits + ' '
#     new_string = ""
#     for character in orig_string:
#         if character in allowed:
#             new_string += character
 
#     return new_string
