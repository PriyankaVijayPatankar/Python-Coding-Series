# Day 54
# Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. Two arrays are said to be disjoint if they have no elements in common.

def DisjointOrNot(arr1,arr2,n1,n2):
    flag = True;
    for i in range(0,n1):
        for j in range(0,n2):
            if arr1[i] == arr2[j] :
                flag = False
        if flag == False :
            break
    return flag

n1 = int(input("Enter aray 1 size: "))
print("Enter array 1 elements: ")
arr1 = list(map(int,input().split(' ')))

n2 = int(input("Enter aray 2 size: "))
print("Enter array 2 elements: ")
arr2 = list(map(int,input().split(' ')))

if DisjointOrNot(arr1,arr2,n1,n2) == True :
    print("Disjoint")
else:
    print("Not disjoint")