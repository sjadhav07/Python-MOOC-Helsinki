# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    a = [letter for letter in string if letter not in forbidden]
    return "".join(a)