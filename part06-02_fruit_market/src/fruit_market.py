# write your solution here
def read_fruits():
    dict = {}
    with open("fruits.csv") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(";")
            dict[line[0]] = float(line[1])
    return dict