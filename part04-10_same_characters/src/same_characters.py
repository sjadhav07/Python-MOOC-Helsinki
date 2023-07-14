# Write your solution here
def same_chars(word, index1, index2):
    length = len(word)
    if index1 >= length or index2 >= length:
        return False
    else:
        return (word[index1] == word[index2])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))