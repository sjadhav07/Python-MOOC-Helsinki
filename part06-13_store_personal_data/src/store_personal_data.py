# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv","w") as f:
        f.write(f"{person[0]};{person[1]};{person[2]}\n")
            
#official solution:
# def store_personal_data(person: tuple):
#     with open("people.csv", "a") as file:
#         row = person[0] + ";"
#         row += str(person[1]) + ";"
#         row += str(person[2])
 
#         file.write(row + "\n")