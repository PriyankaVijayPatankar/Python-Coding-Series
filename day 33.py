# Day 33
# Write a program to check if String is a palindrome or not

s = input("Enter a string: ")
n = len(s)
flag = 0

for i in range(0,n//2):
    if(s[i]==s[n-i-1]):
        flag=+1
if flag==i:
    print("The input string is a Palindrome")
else:
    print("The input string is not a Palindrome")