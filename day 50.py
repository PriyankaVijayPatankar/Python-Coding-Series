# Day 50
# Given an integer array of size N. Write Program to find sum of positive square elements in the array.

n = int(input("Enter the size of array: "))
arr = []
sum = 0

print("Enter the array elements: ")

for i in range(0,n):
    p = int(input())
    arr.append(p)

for j in arr:
    sum = sum + (j**2)

print("Sum of squares: ",sum)
