# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    
    courses = json.loads(data)

    for course in courses:
        hobbies = ", ".join(course['hobbies'])
        print(f"{course['name']} {course['age']} years ({hobbies})")
    
#OFFICIAL SOLUTION:
# import json
# def print_persons(filename: str):
#     with open(filename) as f:
#         content = f.read()
#     persons = json.loads(content)
#     for person in persons:
#         name = person['name']
#         age = person['age']
#         hobbies = ", ".join(person['hobbies'])
#         print(f"{name} {age} years ({hobbies})")