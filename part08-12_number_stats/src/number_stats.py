# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if not self.numbers:
            return 0.0
        else:
            return self.get_sum() / self.count_numbers()
stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    num = int(input("Please type in integer numbers:"))
    if num == -1:
        break
    stats.add_number(num)
    if num % 2 == 0:
        even.add_number(num)
    else:
        odd.add_number(num)
print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")