# Day 42
# Write Program to check if two arrays are the same or not

def check(arr1,arr2,n1,n2):
    count = 0
    arr1.sort()
    arr2.sort()
    for i in range(0,n1):
        if(arr1[i]==arr2[i]):
            count = count + 1
        print(count)
    return count  

n1 = int(input("Enter size of 1st array: "))


n2 = int(input("Enter the size of 2nd array: "))
arr1 = []
print("Enter the elements of 1st array: ")
for i in range(0,n1):
    temp = int(input())
    arr1.append(temp)
arr2 = []
print("Enter the elements of 2nd array: ")
for i in range(0,n2):
    temp = int(input())
    arr2.append(temp)

if (check(arr1,arr2,n1,n2)!=n1):
    print("The input arrays are not same")
else:
    print("The input arrays are same")