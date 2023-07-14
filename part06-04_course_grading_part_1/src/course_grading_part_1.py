# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

names = {}
exercises = {}
with open(student_info) as new_file:
    for lines in new_file:
        lines = lines.split(";")
        if lines[0] == "id":
            continue
        names[lines[0]] = lines[1] + " " + lines[2].replace("\n","")
    
with open(exercise_data) as newer_file:
    for lines in newer_file:
        lst = []
        lines = lines.split(";")
        if lines[0] == "id":
            continue 
        for num in lines[1:]:
            lst.append(int(num))
        exercises[lines[0]] = sum(lst)
for id, name in names.items():
    if id in exercises:
        score = exercises[id]
        print(f"{name} {score}")

