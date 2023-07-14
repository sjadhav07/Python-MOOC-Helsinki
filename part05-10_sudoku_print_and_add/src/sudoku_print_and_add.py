# Write your solution here

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku_new = sudoku[:]
    sudoku_new[row_no][column_no] = number
    sudoku = sudoku_new[:]

def print_sudoku(sudoku: list):
    j = 0
    for row in sudoku:
        if j == 3 or j == 6:
            print()
        for i in range(9):
            if row[i] == 0:
                print("_ ", end = "")
            elif row[i] != 0:
                print(f"{row[i]} ", end = "")
            if i == 2 or i == 5:
                print(" ", end = "")
        j += 1
        print()

# Helsinki MOOC official solution :
# def print_sudoku(sudoku: list):
#   r = 0
#    for row in sudoku:
#        s = 0
#        for character in row:
#            s += 1
#            if character == 0:
#                character = "_"
#            m = f"{character} "
#            if s%3 == 0 and s < 8:
#                m += " "
#            print(m, end="")
# 
#        print()
#        r += 1
#        if r%3 == 0 and r < 8:
#            print()
# 
#def add_number(sudoku: list, row_no: int, column_no: int, number: int):
#    sudoku[row_no][column_no] = number //
