# Day 51
# Given an integer array of size N, write a program to sort the array;

n = int(input("Enter the size of array: "))
arr = []
temp = 0
print("Enter the array elements: ")
for i in range(0,n):
    p = int(input())
    arr.append(p)

for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    
print("Sorted array: ")
for i in range(0,n):
    print(arr[i],end=" ")