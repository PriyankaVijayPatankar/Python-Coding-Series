# Day 23
# Write a program to Replace all 0’s with 1 in a given integer

num = int(input("Enter a number: "))
new = 0

if num==0:
    new = 1

while num>0:
    rem = num % 10
    if rem==0:
        rem = 1
    num = num // 10
    new = (new * 10) + rem

num = 0
while new>0:
    num = (num * 10) + (new % 10)
    new = new // 10

print("New number after replacement is: ",num)