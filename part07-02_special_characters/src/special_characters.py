# Write your solution here
from string import *
def separate_characters(my_string: str):
    first_part = ""
    second_part = ""
    third_part = ""
    for char in my_string:
        if char in ascii_letters:
            first_part += char
        elif char in punctuation:
            second_part += char
        else:
            third_part += char
    return (first_part, second_part, third_part)