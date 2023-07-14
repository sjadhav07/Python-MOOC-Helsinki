# Write your solution here
def factorials(n: int):
    dict = {}
    dict[1] = 1
    for num in range(2, n+1):
        dict[num] = dict[num-1]*num
    return dict
