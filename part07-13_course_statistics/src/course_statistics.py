# Write your solution here
import urllib.request
import json
def retrieve_all():
    #get data from URL (b format)
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)
    #decode from b format to string
    string = str(response.read())
    json_obj = json.loads(string) #json_obj is now in dict format
    course_list = []
    for listing in json_obj:
        # check if course is enabled
        if listing["enabled"] == True:
            course = (listing["fullName"], listing["name"], listing["year"], sum(listing["exercises"]))
            course_list.append(course)
    return course_list

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    string = str(my_request.read())
    jsons_obj = json.loads(string)
    grade_list = []
    students = 0
    hours = 0
    exercises = 0
    weeks = 0
    hours_average = 0
    exercise_average = 0
    for dict in jsons_obj.values():
        weeks += 1
        students += int(dict["students"])
        exercises += int(dict["exercise_total"])
        hours += int(dict["hour_total"])

    dict = {}
    dict['weeks'] = weeks
    dict['students'] = students
    dict['hours'] = hours
    dict['hours_average'] = round(hours / students)
    dict['exercises'] = exercises
    dict['exercises_average'] = round(exercises / students)

    return dict

