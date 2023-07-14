# write your solution here
def largest():
    max = 0
    with open("numbers.txt") as f:
        for line in f:
            line = line.replace("\n","")
            if int(line) > max:
                max = int(line)
    return (max)

#OFFICIAL SOLUTION: 
# def largest():
#     with open("numbers.txt") as file:
#         start = True
#         biggest = 0
#         for number in file:
#             if start or int(number) > biggest:
#                 biggest = int(number)
#                 start = False
#         return biggest
