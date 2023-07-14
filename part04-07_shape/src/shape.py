# Copy here code of line function from previous exercise and use it in your solution
def line(num, letter):
    if letter == "":
        print("*"*num)
    else:
        print(letter[0]*num)
# You can test your function by calling it within the following block
def shape(size,letter, height, filler):
    i = 0
    while i < size:
        i += 1
        line(i, letter)
    
    while height > 0:
        line (size, filler)
        height -= 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")