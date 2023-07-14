# Write your solution here
# adds a student to the database

def add_student(dict, name):
    dict[name] = {}

# prints out information of a single student
def print_student(dict, name):
    if name not in dict:
        print(f"{name}: no such person in the database")
        return
    if len(dict[name]) < 1:
        print(name + ":")
        print(" no completed courses" )
    elif len(dict[name]) >= 1:
        sum = 0
        print(name + ":")
        print(f" {len(dict[name])} completed courses:")
        for subject in dict[name]:
            sum += dict[name][subject]
            print("  ",end="")
            print(subject, dict[name][subject])
        print(f" average grade {sum/len(dict[name])}") 
    

# adds a completed course to information of specific student in database.
# course data is a tuple consisting of name of course and grade
def add_course(dict, name, course):
    if course[1] != 0:
        if course[0] in dict[name]:
            if course[1] > dict[name][course[0]]:
                dict[name][course[0]] = course[1]
        elif course[0] not in dict[name]:
            dict[name][course[0]] = course[1]

# prints out summary based on all information in database
def summary(dict):
    max_course_count = 0
    max_avg_grade = 0
    for item in dict:
        course_count = 0
        total_grade = 0
        for courses in dict[item]:
            course_count += 1
            total_grade += dict[item][courses]
        avg_grade = total_grade / course_count
        if avg_grade > max_avg_grade:
            max_avg_grade = avg_grade
            max_grade_person = item
            
        if course_count > max_course_count:
            max_course_count = course_count
            name = item
        
    print(f"students {len(dict)}")
    print(f"most courses completed {max_course_count} {name}")
    print(f"best average grade {max_avg_grade} {max_grade_person}")




# OFFICIAL SOLUTION:
# TO DO: COMPARE OFFICIAL SOLUTION WITH YOUR OWN    
# def add_student(students: dict, name: str):
#     students[name] = {}
 
# def print_student(students: dict, name: str):
#     if not name in students:
#         print(f"{name}: no such person in the database")
#         return
 
#     students_completed_courses = students[name]
 
#     print(f"{name}:")
#     if len(students_completed_courses) == 0:
#         print(" no completed courses")
#     else:
#         print(f" {len(students_completed_courses):} completed courses:")
#         sum = 0
#         for course, grade in students_completed_courses.items():
#             course_grade = grade[1]
#             print(f"  {course} {course_grade}")
#             sum += course_grade
 
#         print(f" average grade {sum/len(students_completed_courses):.1f}")
 
# def add_course(students: dict, name: str, completion: tuple):
#     students_completed_courses = students[name]
#     course_name = completion[0]
#     course_grade = completion[1]
 
#     # failed course is not recorded in the database
#     if course_grade==0:
#         return
 
#     # if previous grade is higher, new grade is not recorded in the database
#     if course_name in students_completed_courses:
#         if students_completed_courses[course_name][1] > course_grade:
#             return
 
#     students_completed_courses[course_name] = completion
 
# def summary(students: dict):
#     print(f"students {len(students)}")
#     most_courses_count = 0
#     best_avg_grade = 0
#     for name, completions in students.items():
#         if len(completions) > most_courses_count:
#             most_courses = name
#             most_courses_count = len(students[most_courses])
 
#         sum = 0
#         for course, grade in completions.items():
#             sum += grade[1]
 
#         if len(completions)==0:
#             avg = 0
#         else:
#             avg = sum/len(completions)
 
#         if avg>best_avg_grade:
#             best_avg_grade = avg
#             best = name
 
#     print(f"most courses completed {most_courses_count} {most_courses}")
#     print(f"best average grade {best_avg_grade:.1f} {best}")