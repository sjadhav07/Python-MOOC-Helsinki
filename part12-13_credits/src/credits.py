from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, item: reduced_sum+item.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    lst = list(filter(lambda x:x.grade >=1, attempts))
    return reduce(lambda reduced_sum, item: reduced_sum+item.credits, lst, 0)

def average(attempts: list):
     lst = list(filter(lambda x:x.grade >=1, attempts))
     total_score = reduce(lambda reduced_sum, item: reduced_sum+item.grade, lst, 0)
     avg = total_score/len(lst)
     return avg