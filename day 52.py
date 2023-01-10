# Given an integer array of size N, write a program to reverse the array

# Day 51
# Given an integer array of size N, write a program to sort the array;

n = int(input("Enter the size of array: "))
arr = []
print("Enter the array elements: ")
for i in range(0,n):
    p = int(input())
    arr.append(p)

print("Reverse array: ")
for i in range(n-1,-1,-1):
    print(arr[i],end=" ")