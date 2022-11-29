# Day 13
# Write a program to find sum of N natural numbers

n = int(input("Enter the value of n: "))
sum = 0
 
for i in range(1,n+1):
    sum = sum + i
 
print("Sum of n natural numbers is",sum)
