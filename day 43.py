# Day 43
# Write Program to find the array type (odd/even/mixed)

arr1 = []
odd = 0
even = 0
n = int(input("Enter the size of array: "))
print("Enter the elements:")

for i in range(0,n):
    p = int(input())
    arr1.append(p)
    
for i in range(0,n):
    if (arr1[i]%2==0):
        even+=1
    else:
        odd+=1

if even==0:
    print("Odd array")
elif odd==0:
    print("Even array")
else:
    print("Mixed array")
