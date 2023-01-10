# Day 55
# Given 2 integer arrays X and Y of same size. 
# Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

n = int(input("Enter aray size: "))
print("Enter array 1 elements: ")
arr1 = list(map(int,input().split(' ')))

print("Enter array 2 elements: ")
arr2 = list(map(int,input().split(' ')))

prod = 0

for i in range(0,n):
        prod = prod + (arr1[i]*arr2[i])

print("Maximum scalar product: ",prod)