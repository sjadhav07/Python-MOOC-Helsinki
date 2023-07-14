# Write your solution here
def double_items(numbers: list):
    new_list = []
    for num in numbers:
        new_list.append(2*num)
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)