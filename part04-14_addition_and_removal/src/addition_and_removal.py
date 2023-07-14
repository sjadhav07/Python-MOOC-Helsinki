# Write your solution here
list = []
while True:
    print(f"The list is now {list}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        list.insert(len(list), len(list)+1)
    elif command == "r":
        list.pop()
    elif command == "x":
        print("Bye!")
        break