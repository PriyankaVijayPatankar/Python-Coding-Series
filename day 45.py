# Day 45
# Write Program to find smallest and largest element in an array

arr = []

n = int(input("Enter the number of elements in array: "))
print("Enter the array elements: ")

for i in range(0,n):
    p = int(input())
    arr.append(p)

max = arr[0]
min = arr[0]

for j in arr:
    if j > max:
        max = j
    if j < min:
        min = j

print("\nSmallest element in the input array is:",min)
print("\nLargest element in the input array is:",max)




