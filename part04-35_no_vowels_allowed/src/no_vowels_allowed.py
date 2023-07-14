# Write your solution here
def no_vowels(word):
    lst = ['a','e','i','o','u']
    for char in word:
        if char in ['a','e','i','o','u']:
            word = word.replace(char,'')
    return word