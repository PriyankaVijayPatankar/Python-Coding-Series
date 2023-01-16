# Day 56
# Write Program to find whether the numbers of an array be made equal

def convert(a,n):
    for i in range(n):
        while (a[i]%2 == 0):
            a[i] = a[i]/2
        while (a[i]%3 == 0):
            a[i] = a[i]/3

    for i in range (n):
        if a[i] != a[0]:
            return False

    return True

n = int(input("Enter the size of array: "))
arr = []

print("Enter array elements: ")
for i in range(n):
    arr.append(int(input()))
    
if convert(arr,n):
    print("Yes, it is possible")
else:
    print("No, it is not possible")