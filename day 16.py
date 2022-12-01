# Day 16
# Write a program to identify if the number is Perfect number or not

# Example: 
# Let the number be 28, factors of 28 are 1,2,4,7,14. Now the sum of all these factors are 28 itself. Hence, 28 is a perfect number

num = int(input("Enter a number: "))
sum = 0

for i in range (1, num):
    if (num % i == 0):
        sum = sum + i

if (sum==num):
    print("The input number is a perfect number")
else:
    print("The input number is not a perfect number")



