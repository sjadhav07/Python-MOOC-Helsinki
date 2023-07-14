# Write your solution here
def most_common_character(word):
    total = 0
    for char in word:
        if word.count(char) > total:
            total = word.count(char)
            new_char = char
    return new_char