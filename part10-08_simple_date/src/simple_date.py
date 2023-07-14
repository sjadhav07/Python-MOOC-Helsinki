# WRITE YOUR SOLUTION HERE:
class SimpleDate:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        return ((self.day == another.day) and (self.month == another.month) and (self.year == another.year))
        
    def __ne__(self, another):
        return not ((self.day == another.day) and (self.month == another.month) and (self.year == another.year))

    def __lt__(self, another):
        if self.year != another.year:
            if self.year < another.year:
                return True
            return False
        elif self.month != another.month:
            if self.month < another.month:
                return True
            return False
        elif self.day != another.day:
            if self.day < another.day:
                return True
            return False
    def __gt__(self, another):
        return not(self.__lt__(another))
        
    def __add__(self, days: int):
        newdate = SimpleDate(self.day,self.month,self.year)
        if days >= 360:
            year = days // 360
            newdate.year += year
            days -= (360*year)
        if days >= 30:
            month = days // 30
            newdate.month += month
            days -= (30*month)
            if newdate.month > 12:
                ye = newdate.month // 12
                newdate.year += ye
                newdate.month -= (12*ye)
        newdate.day += days
        if newdate.day > 30:
            mo = newdate.day // 30
            newdate.month += mo
            newdate.day -= (30*mo)
        return newdate
    
    def __sub__(self, another):
        total_days = (self.day + self.month*30 + self.year * 360) - (another.day + another.month*30 + another.year * 360)
        return abs(total_days)

#OFFICIAL SOLUTION MUST CHECK:
# class SimpleDate:
#     def __init__(self, pv: int, month: int, year: int):
#         self.__pv = pv
#         self.__month = month
#         self.__year = year
 
#     def __str__(self):
#         return f'{self.__pv}.{self.__month}.{self.__year}'
 
#     # Comparisons are easier, when date is converted to days
#     def __value(self):
#         return self.__year * 360 + self.__month * 30 + self.__pv
 
#     # Converst days back to date
#     def __to_date(self, days: int):
#         months = days // 30
#         years = months // 12
#         days -= months * 30
#         months -= years * 12
#         return SimpleDate(days, months, years)
 
#     def __lt__(self, other: "SimpleDate"):
#         return self.__value() < other.__value()
 
#     def __gt__(self, other: "SimpleDate"):
#         return self.__value() > other.__value()
 
#     def __eq__(self, other: "SimpleDate"):
#         return self.__value() == other.__value()
        
#     def __ne__(self, other: "SimpleDate"):
#         return self.__value() != other.__value()
 
#     def __add__(self, days_to_add: int):
#         return self.__to_date(self.__value() + days_to_add)
 
#     def __sub__(self, other: "SimpleDate"):
#         # abs(x) returns the absolute value of x
#         return abs(self.__value() - other.__value())