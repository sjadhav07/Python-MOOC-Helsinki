# Write your solution here
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s % 3 == 0 and s < 8:
                m += " "
            print(m, end = "")
        print()
        r += 1
        if r % 3 == 0 and r < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    outputSudoku = []
 
    for row in range(len(sudoku)):
        temp = []
        for cell in sudoku[row]:
            temp.append(cell)
        outputSudoku.append(temp)
 
    outputSudoku[row_no][column_no] = number

    return outputSudoku

# OFFICIAL SOLUTION FROM HELSINKI MOOC:
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])  
#     new_list[row_no][column_no] = number
#     return new_list
