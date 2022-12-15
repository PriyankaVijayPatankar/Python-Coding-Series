# Day 30
# Write a Program to print Length of the string without using strlen() function

s = input("Enter a string: ")
count = 0

for i in s:
    count = count + 1
    
print("The length of input string is:",count)