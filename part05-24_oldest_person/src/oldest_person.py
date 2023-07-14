# Write your solution here
def oldest_person(people: list):
    minimum = 3000
    for tple in people:
        if tple[1] < minimum:
            minimum = tple[1]
    for a,b in people:
        if b == minimum:
            return a

# Official Solution: 
#def oldest_person(people: list):
#    oldest = people[0]
#    for person in people:
#       # comparing the year of birth of the oldest known person and the person in turn
#        if person[1] < oldest[1]:
#            oldest = person
# 
#    return oldest[0]