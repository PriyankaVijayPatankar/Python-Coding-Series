# Day 17
# Write a program to find the Factors of a number

num=int(input("Enter a number: "))
print("Factors of input number are as follows:")
for i in range(1,num+1):
    if num%i==0:
        print(i, end=" ")