# Write your solution here
def longest(strings: list):
    word = strings[0]
    for i in range(len(strings)):
        if len(strings[i]) > len(word):
            word = strings[i]
    return word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))