# Day 24
# Write a program to print Pyramid pattern using stars


num = int(input("Enter a number: "))

for i in range(1,(2*num)+1,2):
    for j in range(1,i+1):
        print("*", end=" ")
    print("\n")
    
