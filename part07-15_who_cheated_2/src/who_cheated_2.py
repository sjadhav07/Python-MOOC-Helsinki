# Write your solution here
#OFFICIAL SOLUTION:
import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
         # Then read submissions
         # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
             name = row[0]
             time = datetime.strptime(row[3], "%H:%M")
             # If name does not exists in dictionary, add time directly to the dictionary
             if name not in submission_times:
                 submission_times[name] = time
             # If there alredy exists time for key, compare if current time is greater
             elif time > submission_times[name]:
                 submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
        return cheaters


a = cheaters()
print(a)