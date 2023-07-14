# Write your solution here
def row_sums(my_matrix: list):
    for item in my_matrix:
        item.append(sum(item))