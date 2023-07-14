# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents
        self._money = self._euros + self._cents/100

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"

    def __eq__(self, another):
        return self._money == another._money

    def __lt__(self, another):
        return self._money < another._money
    
    def __gt__(self, another):
        return self._money > another._money
    
    def __ne__(self, another):
        return self._money != another._money
    
    def __add__(self, another):
        money = self._money + another._money
        return "{:.2f}".format(money) + " eur"
    
    def __sub__(self, another):
        if self.__lt__(another):
            raise ValueError(f"a negative result is not allowed")
        else:
            money = (self._money) - (another._money)
            return "{:.2f}".format(money) + " eur"

#OFFICIAL SOLUTION:
# class Money:
#     def __init__(self, euros: int, cents: int):
#         self.__euros = euros
#         self.__cents = cents
 
#     def __str__(self):
#         # f-string has a handy feature for adding leading zeros:
#         # :02d for example means, that output has at least 2 digit
#         return f"{self.__euros}.{self.__cents:02d} eur"
 
#     # Helper method for returning the value in cents
#     # --> makes the comparisons easier
#     def __value(self):
#         return self.__euros * 100 + self.__cents
 
#     # Another helper method which converts cents to value
#     def __set_value(self, cents: int):
#         self.__euros = cents // 100
#         self.__cents = cents - self.__euros * 100
 
#     def __eq__(self, other: "Money"):
#         return self.__value() == other.__value()
 
#     def __lt__(self, other: "Money"):
#         return self.__value() < other.__value()
 
#     def __gt__(self, other: "Money"):
#         return self.__value() > other.__value()
 
#     def __ne__(self, other: "Money"):
#         return self.__value() != other.__value()
 
#     def __add__(self, other: "Money"):
#         msum = Money(0,0)
#         msum.__set_value(self.__value() + other.__value())
#         return msum
 
#     def __sub__(self, other: "Money"):
#         difference = self.__value() - other.__value()
#         if difference < 0:
#             raise ValueError("a negative result is not allowed")
#         dmoney = Money(0,0)
#         dmoney.__set_value(self.__value() - other.__value())
#         return dmoney