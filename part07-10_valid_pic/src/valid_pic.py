# Write your solution here
import datetime
def is_it_valid(pic: str):
    word = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    correctdate = None
    #Create a dictionary and use signs like "-", "+" to point to century like 1900s, 2000s, etc
    dict = {"+":18,"-":19,"A":20}
    try:
        new = datetime.datetime(year = int(str(dict[pic[6]])+pic[4:6]), month = int(pic[2:4]), day = int(pic[:2]))
        correctdate = True
    except:
        correctdate = False
    if correctdate and pic[6] in ["+","-","A"] and word[(int(pic[:6] + pic[7:10]) % 31)] == pic[-1] and len(pic) == 11:
        return True
    else:
        return False
#OFFICIAL CODE:
# def is_it_valid(pic: str):
#     if len(pic) != 11:
#         return False
#     numbers = pic[:6]+pic[7:10]
#     for x in numbers:
#         if x not in "0123456789":
#             return False
#     century_marker = pic[6]
#     if century_marker not in "+-A":
#         return False
#     day = int(pic[:2])
#     month = int(pic[2:4])
#     year = int(pic[4:6])
#     if century_marker == "+":
#         year += 1800
#     if century_marker == "-":
#         year += 1900
#     if century_marker == "A":
#         year += 2000
#     try:
#         test = datetime(year, month, day)
#     except:
#         return False
#     characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
#     index = int(numbers)%31
#     return characters[index] == pic[-1]