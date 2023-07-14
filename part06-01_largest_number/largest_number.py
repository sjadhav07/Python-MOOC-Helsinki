# write your solution here
def largest():
    max = 0
    with open("numbers.txt") as f:
        for line in f.read():
            line = line.replace("\n","")
            if int(line) > max:
                max = int(line)
    print(max)

