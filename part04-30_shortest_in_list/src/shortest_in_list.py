# Write your solution here
def shortest(mylist):
    short = mylist[0]
    for word in mylist:
        if len(word) < len(short):
            short = word
    return short
    