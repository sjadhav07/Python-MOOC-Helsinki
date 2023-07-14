# Write your solution here
# Get
def longest_series_of_neighbours(lst: list):
    new_list = []
    for i in range(1,len(lst)):
        if lst[i] - lst[i-1] > 1 :
            new_list.append(lst[i])