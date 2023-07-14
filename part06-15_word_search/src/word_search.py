def read_file():
    lst = []
    word_list = []
    with open("words.txt","r") as f:
        for lines in f:
            lines = lines.replace("\n","")
            word_list.append(lines)
    return word_list
def find_words(search_term: str):
    word_list = read_file()
    lst = []
    if "." in search_term:
        for words in word_list:
            if len(search_term) == len(words):
                for i in range(len(search_term)):
                    if i == len(words)-1 and search_term[i] == ".":
                        lst.append(words)
                        
                    elif search_term[i] == '.':
                        continue
                    elif search_term[i] != words[i]:
                        break
                    elif i == len(words)-1:
                        lst.append(words)
    elif search_term.endswith("*"): 
        word_list = read_file()
        for words in word_list:
            if search_term[:-1] == words[:len(search_term)-1]:
                lst.append(words)
    elif search_term.startswith("*"):
        word_list = read_file()
        for words in word_list:
            #TO DO : How was this solved in official solution?
            if search_term[1:] == words[-len(search_term)+1:]:
                lst.append(words)
    else:
        word_list = read_file()
        for words in word_list:
            if search_term == words:
                lst.append(words)
    return lst

#OFFICIAL SOLUTION: TO DO: CHECK HOW THE PROBLEMS WERE SOLVED
# def find_words(search_term: str):
#     results = []
 
#     with open("words.txt") as file:
#         # Tätä tarvitaan myöhemmin
#         hakusana_ilman_tahtea = search_term.replace("*","")
 
#         for word in file:
#             word = word.replace("\n","")
#             # Is there an asterisk?
#             if "*" in search_term:
#                 # start or end?
#                 if search_term[0] == "*":
#                     if word.endswith(hakusana_ilman_tahtea):
#                         results.append(word)
#                 else:
#                     if word.startswith(hakusana_ilman_tahtea):
#                         results.append(word)
#             # Is there a dot?
#             elif "." in search_term:
#                 # same length?
#                 if len(search_term) == len(word):
#                     found = True
#                     for i in range(len(search_term)):
#                         if search_term[i] != "." and search_term[i] != word[i]:
#                             found = False
#                             break
#                     if found:
#                         results.append(word)
#             # No special characters, only whole word matches count
#             else:
#                 if word == search_term:
#                     results.append(word)
#     return results


