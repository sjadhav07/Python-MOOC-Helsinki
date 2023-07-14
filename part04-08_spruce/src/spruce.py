# Write your solution here
def spruce(size):
    num = 1
    base = size
    print("a spruce!")
    while size > 0:
        print(" "*(size-1),end = "")
        print("*"*num)
        size -= 1
        num += 2
    print(" "*(base-1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)