# Day 12 
# Write a program to find Sum of digits of a number

num = int(input("Enter a number: "))
sum = 0
 
while num!=0:
    i = num % 10
    sum = sum + i
    num = num // 10
 
print("Sum of the digits is",sum)
