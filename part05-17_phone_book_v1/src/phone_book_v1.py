# Write your solution here. This is offical solution:

def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")

def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")

def main():
    persons = {}
    while True:
        cmd = int(input("command (1 search, 2 add, 3 quit): "))
        if cmd == 1:
            search(persons)
        if cmd == 2:
            add(persons)
        if cmd == 3:
            break
    print("quitting...")

main()
