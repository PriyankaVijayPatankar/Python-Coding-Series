# Day 15
# Write a program to identify if the number is Strong number or not

num = int(input("Enter a number: "))
org = num
sum = 0

while(num):
    fact = 1
    i = 1
    n1 = num % 10

    while (i<=n1):
        fact = fact * i
        i = i + 1

    sum = sum + fact
    num = num // 10

if (sum == org):
    print("Input number is a Strong Number")
else: 
    print("Input number is not a Strong Number")