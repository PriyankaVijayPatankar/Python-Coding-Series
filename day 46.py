# Day 46
# Write Program to find sum of elements in an array

n = int(input("Enter the size of array: "))
arr = []
sum = 0

print("Enter the elements of array: ")
for i in range(n):
    p = int(input())
    arr.append(p)

for j in arr:
    sum = sum + j

print("Sum of elements in the given array is:",sum)

