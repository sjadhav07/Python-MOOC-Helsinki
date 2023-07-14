# Write your solution here

def sudoku_grid_correct(sudoku: list):
    numbers = []
    
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)

    col_numbers = []
    for row in sudoku:
        for column_no in range(9):
            if row[column_no] > 0 and row[column_no] in col_numbers:
                return False
            col_numbers.append(row[column_no])


    l = 0
    row_numbers = []
    for row in sudoku:
        for i in range(9):
            if row[i] > 0 and row[i] in row_numbers:
                return False
            row_numbers.append(row[i])

    return True
