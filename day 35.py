# Day 35
# Write a program to count the sum of numbers in a string 

num = input("Enter a number: ")
sum = 0

for i in num:
    if (ord(i)>=48 and ord(i)<=57):
        sum = sum + int(i)

print("Sum of numbers is:",sum)
