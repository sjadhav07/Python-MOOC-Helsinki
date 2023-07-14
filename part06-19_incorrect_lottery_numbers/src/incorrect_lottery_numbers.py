# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv","r") as f:
        with open("correct_numbers.csv","w") as fo:
                for lines in f:
                    lines = lines.replace("\n","")
                    new_lines = lines.split(";")
                    try:
                        if 1 <= int(new_lines[0].split()[1]) <= 52 and len(new_lines[1].split(",")) > 6:    
                            for numbers in new_lines[1].split(","):
                                if 1 <= int(numbers) <= 39 and ("." not in numbers):
                                    condition = True
                            if condition:
                                fo.write(lines+"\n")
                    except:
                        pass
#OFFICIAL SOLUTION:
# def filter_incorrect():
#     with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
#         for row in input_file:
#             parts = row.strip().split(";")
#             if len(parts) != 2:
#                 continue
#             week = parts[0].split(" ")
#             error = False
#             if len(week) != 2 or week[0] != "week":
#                 error = True
#             try:
#                 mika = int(week[1])
#             except:
#                 error = True
#             number_list = parts[1].split(",")
#             if len(number_list) != 7:
#                 error = True
 
#             # numbers already listed --> to find out duplicates
#             listed = []
#             for item in number_list:
#                 try:
#                     number = int(item)
#                     if number < 1 or number > 39 or number in listed:
#                         error = True
#                     listed.append(number)
#                 except:
#                     error = True
#             if not error:
#                 result_file.write(row)