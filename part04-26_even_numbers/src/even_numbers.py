# Write your solution here
def even_numbers(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list