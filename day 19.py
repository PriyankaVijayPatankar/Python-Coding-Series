# Day 19
# Write a program to identify if the number is Armstrong number or not

num = int(input("Enter a number: "))
org = num
sum = 0

while(num>0):
    digit = num % 10
    sum = sum + (digit ** 3)
    num = num // 10

if (sum == org):
    print("Input number is an Armstrong Number")
else: 
    print("Input number is not an Armstrong Number")