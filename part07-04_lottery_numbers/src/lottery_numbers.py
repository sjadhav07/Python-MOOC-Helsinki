# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    return sorted(sample(list(range(lower,upper+1)), amount))

#OFFICIAL SOLUTION:
# from random import randint 
# def lottery_numbers(amount: int, lower: int, upper: int):
#     numbers = []
#     while len(numbers) < amount:
#         number = randint(lower, upper)
#         if number not in numbers:
#             numbers.append(number)
#     return sorted(numbers)
