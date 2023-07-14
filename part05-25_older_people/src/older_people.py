# Write your solution here
def older_people(people: list, year: int):
    lst = []
    for tple in people:
        if tple[1] < year:
            lst.append(tple[0])
    return lst