# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    checksum = 0
    for i in range(len(my_matrix)):
        for num in my_matrix[i]:
            if num == element:
                checksum += 1
    return checksum

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))