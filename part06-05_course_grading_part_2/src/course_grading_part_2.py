# wwite your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
names = {}
exercises = {}
points = {}
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

with open(exam_points) as exam_points_file:
    for lines in exam_points_file:
        lst = []
        lines = lines.split(";")
        if lines[0] == "id":
            continue
        for num in lines[1:]:
            lst.append(int(num))
        points[lines[0]] = sum(lst)

for id, name in names.items():
    if id in exercises and id in points:
        exercise_score = int(exercises[id]/4)
        points_score = points[id]
        final_score = exercise_score + points_score
        if final_score < 15:
            final_grade = 0
        elif 14 < final_score < 18:
            final_grade = 1
        elif 17 < final_score < 21:
            final_grade = 2
        elif 20 < final_score < 24:
            final_grade = 3
        elif 23 < final_score < 27:
            final_grade = 4
        else:
            final_grade = 5
        print(f"{name} {final_grade}")

    
#OFFICIAL SOLUTION: NOTICE THE FUCNTIONS TO REDUCE THE CODE
# student_data = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_data = input("Exam points: ")
 
# def grade(points):
#     a = 0
#     limits = [15, 18, 21, 24, 28]
#     while a < 5 and points >= limits[a]:
#         a += 1
 
#     return a
 
# def to_points(number):
#     return number // 4
 
# students = {}
# with open(student_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue
#         students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
# exercises = {}
# with open(exercise_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue
#         esum = 0
#         for i in range(1, 8):
#             esum += int(parts[i])
#         exercises[parts[0]] = esum
 
# exams = {}
# with open(exam_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue 
#         esum = 0
#         for i in range(1, 4):
#             esum += int(parts[i])
#         exams[parts[0]] = esum
 
# for student_id, name in students.items():
#     total = exams[student_id] + to_points(exercises[student_id])
#     print(f"{name} {grade(total)}")