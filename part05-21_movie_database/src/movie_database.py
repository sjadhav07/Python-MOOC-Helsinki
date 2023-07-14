# Write your solution here
from cProfile import run


def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie["name"] = name
    movie["director"] = director
    movie["year"] = year
    movie["runtime"] = runtime
    database.append(movie)

#OFFICIAL solution: 
#def add_movie(database: list, name: str, director: str, year: int, runtime: int):
#    # Python accepts splitting rows from punctuation
#    # The addition becomes more readable when parts are divided into separate rows
#    movie = {"name": name,
#               "director": director,
#               "year": year,
#               "runtime": runtime}
# 
#    database.append(movie)
# Write your solution here