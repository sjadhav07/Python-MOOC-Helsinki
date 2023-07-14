# Write your solution here
num = int(input("Please type in a positive number: "))
for num in range(-num,num+1):
    if num == 0:
        continue
    print(num)
