# Write your solution here
def filter_solutions():
    correct_lst = []
    incorrect_lst = []
    with open("solutions.csv") as f:
        for lines in f:
            lines = lines.replace("\n","")
            lines_new = lines.split(";")
            operator = ['+','-']
            if operator[0] in lines_new[1]:
                numbers = lines_new[1].split(operator[0])
                if (int(numbers[0]) + int(numbers[1])) == int(lines_new[2]):
                    correct_lst.append(lines)
                else:
                    incorrect_lst.append(lines)
            elif operator[1] in lines_new[1]:
                numbers = lines_new[1].split(operator[1])
                if (int(numbers[0]) - int(numbers[1])) == int(lines_new[2]):
                    correct_lst.append(lines)
                else:
                    incorrect_lst.append(lines)
    with open("correct.csv","w") as f:
        for elements in correct_lst:
            f.write(elements+"\n")
    with open("incorrect.csv","w") as f:
        for elements in incorrect_lst:
            f.write(elements+"\n")

#OFFICIAL SOLUTION: TO DO: CHECK THE CODE STRUCTURE
# def filter_solutions():
#     # Open all lines
#     with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
#         for row in source:
#             # Split into pieces
#             pieces = row.split(";")
 
#             calculation = pieces[1]
#             result = pieces[2]
 
#             # Addition or subtraction?
#             if "+" in calculation:
#                 operands = calculation.split("+")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) + int(operands[1]) == int(result)
#             else:
#                 operands = calculation.split("-")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) - int(operands[1]) == int(result)
 
#             # Write to file
#             if correct:
#                 correct_file.write(row)
#             else:
#                 incorrect_file.write(row)