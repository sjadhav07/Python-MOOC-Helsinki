# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
    lst = []
    for num in range(amount):
        lst.append(Fraction(1,amount))
    return lst

#OFFICIAL SOLUTION:
# from fractions import Fraction
# def fractionate(amount: int):
#     # numerator, denominator
#     fraction = Fraction(1, amount)
#     return [fraction] * amount