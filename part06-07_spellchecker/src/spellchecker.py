# write your solution here
word = input("Write text: ")
lst = []
with open("wordlist.txt") as file:
    for lines in file:
        lines = lines.replace("\n","")
        lst.append(lines)
    for words in word.split():
        if words.lower() not in lst:
            words = f"*{words}*"
        print(f"{words} ",end="")
    
#OFFICIAL SOLUTION: NOTICE HOW THE CODE IS ARRANGED 
# def wordlist():
#     words = []
 
#     with open("wordlist.txt") as file:
#         for row in file:
#             words.append(row.strip())
 
#     return words
 
# words = wordlist()
# sentence = input("Write text: ")
 
# for word in sentence.split(' '):
#     if word.lower() in words:
#         print(word + " ", end="")
#     else:
#         print("*" + word + "* ", end="")
 
# print()