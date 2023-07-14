# Write your solution here
from collections import defaultdict


def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")
def add(persons):
    name = input("name: ")
    number = input("number: ")
    data = []
    data.append((name,number))
    for name,number in data:
        persons[name].append(number)
    print("ok!")

def main():
    persons = defaultdict(list)
    
    while True:
        cmd = int(input("(command (1 search, 2 add, 3 quit): "))
        if cmd == 1:
            search(persons)
        if cmd == 2:
            add(persons)    
        if cmd == 3:
            break
    print("quitting...")
    
main()