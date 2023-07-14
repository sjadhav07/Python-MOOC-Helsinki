# Copy here code of line function from previous exercise
def line(num, letter):
    if letter == "":
        print("*"*num)
    else:
        print(letter[0]*num)

def square(size, character):
    # You should call function line here with proper parameters
    row = size
    while size > 0:
        line(row, character)
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")