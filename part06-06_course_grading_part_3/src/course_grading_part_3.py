# tee ratkaisu tänne
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
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
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
        
        print(f"{name:<30}{exercises[id]:<10}{exercise_score:<10}{points_score:<10}{final_score:<10}{final_grade:<10}")
