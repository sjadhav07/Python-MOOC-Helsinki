# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    if person1["result1"]+person1["result2"]+person1["result3"] < person2["result1"]+person2["result2"]+person2["result3"] and person1["result1"]+person1["result2"]+person1["result3"] < person3["result1"]+person3["result2"]+person3["result3"]:
        return person1
    elif person2["result1"]+person2["result2"]+person2["result3"] < person1["result1"]+person1["result2"]+person1["result3"] and person2["result1"]+person2["result2"]+person2["result3"] < person3["result1"]+person3["result2"]+person3["result3"]:
        return person2
    else:
        return person3
        
#OFFICIAL SOLUTION:
# def average(person: dict):
#     ex_sum = person["result1"]+person["result2"]+person["result3"]
#     return ex_sum/3
 
# def smallest_average(person1: dict, person2: dict, person3: dict):
#     smallest = person1
 
#     if average(person2) < average(smallest):
#         smallest = person2
 
#     if average(person3) < average(smallest):
#         smallest = person3
 
#     return smallest