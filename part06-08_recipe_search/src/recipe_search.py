# Write your solution here
def end_lst(filename: str):
    final_lst = []
    with open(filename) as f:
        lst = []
        for lines in f:
            lines = lines.replace("\n","")
            if lines == "":
                lst = []
                continue
            else:
                lst.append(lines)
            final_lst.append(lst)
    for element in final_lst:
        while final_lst.count(element) > 1:
            final_lst.remove(element)
    return final_lst

# How would I solve this in shorter code?
def search_by_name(filename: str, word: str):
    final_lst = end_lst(filename)
    recope_lst = []
    for small_lst in final_lst:
        if word.lower() in small_lst[0].lower():
            recope_lst.append(small_lst[0])
    return recope_lst

#how were the lists created?
def search_by_time(filename: str, prep_time: int):
    final_lst = end_lst(filename)
    recipe_lst = []
    for small_lst in final_lst:
        if int(small_lst[1]) <= prep_time:
            recipe_lst.append(small_lst[0]+f", preparation time {small_lst[1]} min")
    return recipe_lst
            
def search_by_ingredient(filename: str, ingredient: str):
    final_lst = end_lst(filename)
    recipie_lst = []
    for small_lst in final_lst:
        for i in range(len(small_lst)-2):
            if small_lst[i+2] == ingredient:
                recipie_lst.append(small_lst[0]+f", preparation time {small_lst[1]} min")
    return recipie_lst

#OFFICIAL SOLUTION: 
# def read_file(filename):
#     with open(filename) as file:
#         rows = []
#         for row in file:
#             rows.append(row.strip())
 
#     recipes = []
#     name_in_row = True
#     prep_time_in_row = True
#     new = { "ingredients": []}
#     for row in rows:
#         if name_in_row:
#             new["name"] = row
#             name_in_row = False
#             prep_time_in_row = True
#         elif prep_time_in_row:
#             new["prep_time"] = int(row)
#             prep_time_in_row = False
#         elif len(row) > 0:
#             new["ingredients"].append(row)
#         else:
#             recipes.append(new)
#             name_in_row = True
#             new = {"ingredients": []}
#     recipes.append(new)
 
#     return recipes
 
# def search_by_name(filename: str, word: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if word.lower() in recipe["name"].lower():
#             found.append(recipe["name"])
 
#     return found
 
# def search_by_time(filename: str, time: int):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if recipe["prep_time"] <= time:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found
 
# def search_by_ingredient(filename: str, ingredient: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if ingredient.lower() in recipe["ingredients"]:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found