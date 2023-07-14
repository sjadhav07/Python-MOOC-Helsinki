# Write your solution here
def sum_of_positives(list):
    sum = 0
    for num in list:
        if num > 0:
            sum += num
    return sum