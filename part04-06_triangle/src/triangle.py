# Copy here code of line function from previous exercise
def line(num, letter):
    if letter == "":
        print("*"*num)
    else:
        print(letter[0]*num)

def triangle(size):
    # You should call function line here with proper parameters
    height = size
    while size < (2*height)+1:
        line(size-height, "#")
        size += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
