# Day 21
# Write a program to identify if the number is palindrome number or not

num = int(input("Enter a number: "))
org = num
rev = 0

while num!=0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

if (rev == org):
    print("Input number is a Palindrome")
else: 
    print("Input number is not a Palindrome")