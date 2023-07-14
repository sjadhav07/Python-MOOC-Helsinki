# Write your solution here


result = []

# Get your number of layers
layer = int(input("Give a number between 2 and 26: "))

for i in range(layer):
    # update existing rows
    for j, string in enumerate(result):
        result[j] = chr(65+i) + string + chr(65+i)

    # add top and bottom row
    result.append((2*i+1)*chr(65+i))
    if i != 0:
        result.insert(0, (2*i+1)*chr(65+i))
        
# print result
for line in result:
    print(line)