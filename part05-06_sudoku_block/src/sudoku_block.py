# Write your solution here
# Solve it again using just one list instead of three
def block_correct(sudoku: list,row_no: int, column_no: int):
    lst = []
    new_lst = []
    orig_lst = []
    for num in sudoku[row_no:row_no+3]:
        lst.append(num)
    for row in lst:
        new_lst.append(row[column_no:column_no+3])
    for element in new_lst:
        for item in element:
            if item > 0 and item in orig_lst:
                return False
            orig_lst.append(item)
    return True
