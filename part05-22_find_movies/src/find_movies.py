# Write your solution here
def find_movies(database: list, search_term: str):
    lst = []
    for i in range(len(database)):
        if search_term.lower() in database[i]["name"].lower():
            lst.append(database[i])
    return lst


