# Write your solution here
import string

def histogram(word: string):
    dict = {}
    for letter in list(set(list(word))):
        dict[letter] = "*"*list(word).count(letter)
    for keys, values in dict.items():
        print(f"{keys} {values}")