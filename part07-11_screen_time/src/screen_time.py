# Write your solution here
from datetime import datetime,timedelta
lst = []
file = input("Filename: ")
st_date = input("Starting date: ")
start_date = datetime.strptime(st_date, "%d.%m.%Y") 
day = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ")
begining_date = start_date.strftime("%d.%m.%Y")
end_date = start_date + timedelta(days=day-1)
end_date = end_date.strftime("%d.%m.%Y")

starting_date = start_date
for num in range(day):
    one_day = timedelta(days=1)
    timer = input(f"Screen time {starting_date}: ")
    lst.append(timer)
    starting_date += one_day
print("Data stored in file late_june.txt")

total_min = 0
for item in lst:
    for minutes in item.split():
        total_min += int(minutes)

with open(file,"w") as f:
    f.write(f"Time period: {begining_date}-{end_date}\n")
    f.write(f"Total minutes: {total_min}\n")
    f.write(f"Average minutes: {total_min/day}\n")
    count = 0
    starting = start_date
    for num in range(day):
        lst[count] = lst[count].replace(" ","/")
        start = starting.strftime("%d.%m.%Y")
        f.write(f"{start}: {lst[count]}\n")
        one_day = timedelta(days=1)
        starting += one_day
        count += 1

#OFFICIAL SOLUTION:
# from datetime import datetime, timedelta
 
# week = timedelta(days=7)
 
# def format(aika):
#     return aika.strftime("%d.%m.%Y")
 
# file = input("Filename: ")
# start = input("Starting date: ").split('.')
# days = int(input("How many days: "))
# print("Please type in screen time in minutes on each day (TV computer mobile):")
 
# screen_times = []
# total = 0
# start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
# for i in range(days):
#     day = start + timedelta(days=i)
#     times = input(f"Screen time {format(day)}: ").split(' ')
#     tv = int(times[0])
#     pc = int(times[1])
#     mobile = int(times[2])
#     total += tv + pc + mobile
#     screen_times.append((day, tv, pc, mobile) )
 
# with open(file, "w") as tdsto:
#     tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
#     tdsto.write(f"Total minutes: {total}\n")
#     tdsto.write(f"Average minutes: {total/days:.1f}\n")
#     for pv, tv, pc, mob in screen_times:
#         tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
# print(f"Data stored in file {file}")