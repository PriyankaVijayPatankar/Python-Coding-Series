# Day 48
# Write Program to remove duplicate elements from an array

def removeDup(arr, n):
    if n == 0 or n == 1:
        return n

    temp = list(range(n))
    j = 0

    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[n-1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
    return j;

n = int(input("Enter size of array: "))
arr = []

print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)

n = removeDup(arr, n)

print("After removing duplicate elements, the array is: ")
for i in range(n):
    print ("%d"%(arr[i]), end = " ")