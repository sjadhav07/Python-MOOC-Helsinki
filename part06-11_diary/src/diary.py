# Write your solution here
choice = -1
while choice != 0:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = int(input("Function: "))
    if choice == 1:
        entry = input("Diary entry: ")
        with open("diary.txt","a") as f:
            f.write(entry+"\n")
            print("Diary saved\n")
    elif choice == 2:
        print("Entries: ")
        with open("diary.txt","r") as f:
            for lines in f:
                print(lines,end="")
print("Bye now!")

#OFFICIAL SOLUTION:
# with open("diary.txt") as file:
#     content = []
#     for row in file:
#         content.append(row.replace("\n",""))
 
# # Open file for appending
# with open("diary.txt", "a") as file:
#     while True:
#         print("1 - add an entry, 2 - read entries, 0 - quit")
#         function = input("Function: ")
#         if function == "1":
#             entry = input("Diary entry: ")
#             file.write(entry + "\n")
#             content.append(entry)
#             print("Diary saved")
#         elif function == "2":
#             print("Entries:")
#             for entry in content:
#                 print(entry)
#         elif function == "0":
#             print("Bye now!")
#             break

