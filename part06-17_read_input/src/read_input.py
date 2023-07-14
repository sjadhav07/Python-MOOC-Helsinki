# Write your solution here
def read_input(line: str, a: int, b: int):
    while True:
        try:
            input_str = input(line)
            number = int(input_str)
            if a <= number <= b:
                return number
        except ValueError:
            pass # this command doesn't actually do anything
        print(f"You must type in an integer between {a} and {b}")
    return number

#OFFICIAL SOLUTION: 
# def read_input(prompt: str, lower_limit: int, upper_limit: int):
#     while True:
#         error = False
#         try:
#             number = int(input(prompt))
#             if number < lower_limit or number > upper_limit:
#                 error = True
#         except:
#             error = True
#         if error:
#             print(f"You must type in an integer between {lower_limit} and {upper_limit}")
#         else:
#             return number
