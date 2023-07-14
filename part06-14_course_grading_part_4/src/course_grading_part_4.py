# tee ratkaisu tänne
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")
names = {}
exercises = {}
points = {}
lstcourse = []
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
with open(course_info) as course_file:
    for lines in course_file:
        lines = lines.replace("\n","")
        lstcourse.append(lines)

# print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
# for id, name in names.items():
#     if id in exercises and id in points:
#         exercise_score = int(exercises[id]/4)
#         points_score = points[id]
#         final_score = exercise_score + points_score
#         if final_score < 15:
#             final_grade = 0
#         elif 14 < final_score < 18:
#             final_grade = 1
#         elif 17 < final_score < 21:
#             final_grade = 2
#         elif 20 < final_score < 24:
#             final_grade = 3
#         elif 23 < final_score < 27:
#             final_grade = 4
#         else:
#             final_grade = 5
#         print(f"{name:<30}{exercises[id]:<10}{exercise_score:<10}{points_score:<10}{final_score:<10}{final_grade:<10}")

with open("results.txt", "w") as f:
    f.write(f"{lstcourse[0][6:]}, {lstcourse[1][15]} credits\n")
    f.write("======================================\n")
    f.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
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
            f.write(f"{name:<30}{exercises[id]:<10}{exercise_score:<10}{points_score:<10}{final_score:<10}{final_grade:<10}\n")
#HOW DO I WRITE TO RESULTS.TXT WIHOUT A NEW LINE AFTER EVERY NEW TEXT


with open("results.csv","w") as f:
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
            f.write(f"{id};{name};{final_grade}\n")
print("Results written to files results.txt and results.csv")


# OFFICIAL SOLUTION:
# student_data = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_data = input("Exam points: ")
# course_data = input("Course information: ")
 
# def get_grade(points):
#     a = 0
#     limits = [15, 18, 21, 24, 28]
#     while a < 5 and points >= limits[a]:
#         a += 1
#     return a
 
# def as_score(number):
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
 
# with open(course_data) as file:
#     rows = []
#     for row in file:
#         rows.append(row)
 
#     course_name = rows[0][5:].strip()
#     credits = int(rows[1][14:])
 
# with open("results.txt", "w") as file:
#     header = f"{course_name}, {credits} credits\n"
#     file.write(header)
#     separator = "="*(len(header)-1)
#     file.write(f"{separator}\n")
#     file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
#     for student_id, name in students.items():
#         exer = exercises[student_id]
#         exer_score = as_score(exer)
#         exam_pts = exams[student_id]
#         tot_score = exer_score + exam_pts
#         file.write(f"{name:30}{exer:<10}{exer_score:<10}{exam_pts:<10}{tot_score:<10}{get_grade(tot_score):<10}\n")
 
# with open("results.csv", "w") as file:
#     for student_id, name in students.items():
#         exer = exercises[student_id]
#         exer_score = as_score(exer)
#         exam_pts = exams[student_id]
#         tot_score = exer_score + exam_pts
#         row = ";".join([student_id, name, str(get_grade(tot_score))])
#         file.write(f"{row}\n")