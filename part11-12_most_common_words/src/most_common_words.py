# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    strin = ""
    with open(filename) as f:
        for lines in f:
            strin += lines
    strin = strin.replace(",","")
    strin = strin.replace(".","")
    lst = strin.split()
    return {word : lst.count(word) for word in lst if lst.count(word) >= lower_limit}


#OFFICIAL SOLUTION:
# from string import punctuation
 
# def most_common_words(filename: str, lower_limit: int):
#     with open(filename) as f:
#         content = f.read()
 
#         # remove line breaks and punctuation
#         content = content.replace("\n", " ")
#         for punctuation_mark in punctuation:
#             content = content.replace(punctuation_mark, "")
 
#         words = content.split(" ")
#         return {word: words.count(word) for word in words if words.count(word) >= lower_limit}