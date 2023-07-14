# Write your solution here
def length_of_longest(mylist):
    longest = mylist[0]
    for word in mylist:
        if len(word) > len(longest):
            longest = word
    return len(longest)