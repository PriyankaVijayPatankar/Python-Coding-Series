# Day 14
# Write a program to reverse a given number

num = int(input("Enter a number: "))
rev = 0

while (num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print("Reverse of the input number is",rev)
