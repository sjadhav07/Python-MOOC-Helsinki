# tee ratkaisusi tänne
class StudentDatabase:
    def __init__(self):
        self.__person = {}
    
    def add_course(self, course_name, grading, crediting):
        if course_name not in self.__person:
            self.__person[course_name] = Course(course_name, grading, crediting)
        elif course_name in self.__person:
            if self.__person[course_name].grade < grading:
                self.__person[course_name] = Course(course_name, grading, crediting)
    
    def get_course_data(self, course_name):
        if course_name not in self.__person:
            return None
        return self.__person[course_name]
    
    def stats(self):
        if len(self.__person) != 0:
            return self.__person
    
class StudentDatabaseApplication:
    def __init__(self):
        self.__studentdatabase = StudentDatabase()
    def add_course(self):
        course = input("course: ")
        grading = int(input("grade: "))
        crediting = int(input("credits: "))
        self.__studentdatabase.add_course(course, grading, crediting)
    
    def get_course_data(self):
        course = input("course: ")
        data = self.__studentdatabase.get_course_data(course)
        if data == None:
            print("no entry for this course")
        else:
            print(f"{data.name} ({data.credits} cr) grade {data.grade}")
        
    def statistics(self):
        data = self.__studentdatabase.stats()
        credit = 0
        grade = 0
        lst = []
        for item in data:
            credit += data[item].credits 
            grade += data[item].grade
            lst.append(data[item].grade)
        avg = float(grade/len(data))
        
        

        print(f"{len(data)} completed courses, a total of {credit} credits")
        print("mean {:.1f}".format(avg))
        print("grade distribution")
        
        for item in range(5,0,-1):
            print(f"{item}: "+ "x"*lst.count(item))


    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

class Course:
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = grade
        self.credits = credits

application = StudentDatabaseApplication()
application.execute()