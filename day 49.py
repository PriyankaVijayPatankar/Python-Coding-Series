# Day 49
# Given 2 integer arrays X and Y of same size. 
# Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.

n = int(input("Enter the size of array: "))

X = []
Y = []

print("Enter the array1 elements: ")
for i in range(0,n):
    p = int(input())
    X.append(p)

print("Enter the array2 elements: ")
for i in range(0,n):
    p = int(input())
    Y.append(p)

prod = 0

for j in range(0,n):
    prod = prod + (X[j] * Y[n-1-j])

print("Minimum scalar product of given vectors is: ",prod)

