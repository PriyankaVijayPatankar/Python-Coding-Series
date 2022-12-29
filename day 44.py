# Day 44
# Write Program to find number of even and odd elements in an array

arr=[]
count_e=0
count_o=0

n = int(input("Enter the size of array: "))
print("Enter the elements: ")

for i in range(0,n):
    p = int(input())
    arr.append(p)

for j in arr:
    if j%2==0:
        count_e+=1
    else:
        count_o+=1

print("Number of even elements:", count_e)
print("Number of odd elements:", count_o)


