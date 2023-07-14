# Write your solution here
points = []
exercises = []
passing = 0
fail = 0
total = 0
counti = 0
grade0 = 0
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
grade5 = 0
while True:
    points_exercises = input("Exam points and exercises completed: ")
    if points_exercises == "":
        break
    points.append(int(points_exercises.split()[0]))
    exercises.append(int(points_exercises.split()[1]))
    counti += 1
    
for i in range(counti):
    total += points[i]+exercises[i]//10
    if 0 <= points[i]+exercises[i]//10 <= 14:
        grade0 += 1
        fail += 1
    elif points[i] < 10:
        fail += 1
        grade0 += 1
        continue
    elif 15 <= points[i]+exercises[i]//10 <= 17:
        grade1 += 1
        passing += 1
    elif 17 <= points[i]+exercises[i]//10 <= 20:
        grade2 += 1
        passing += 1
    elif 21 <= points[i]+exercises[i]//10 <= 23:
        grade3 += 1
        passing += 1
    elif 24 <= points[i]+exercises[i]//10 <= 27:
        grade4 += 1
        passing += 1
    elif 28 <= points[i]+exercises[i]//10 <= 30:
        grade5 += 1
        passing += 1
print("Statistics: ")
print(f"Points average: {total/counti}")
print(f"Pass percentage: {(passing/(fail+passing))*100:.1f}")
print("Grade distribution:")
print("  5: " + "*"*grade5)
print("  4: " + "*"*grade4)
print("  3: " + "*"*grade3)
print("  2: " + "*"*grade2)
print("  1: " + "*"*grade1)
print("  0: " + "*"*grade0)