# Write your solution here
items = int(input("How many items: "))
list = []
while items > 0:
    num = int(input(f"Item {items}: "))
    list.append(num)
    items -= 1
print(list)