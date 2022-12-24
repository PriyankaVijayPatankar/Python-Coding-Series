# Day 36
# Write a program to Capitalise the first and last letter of each word of a string

s = input("Enter a string: ")
length = len(s)

s = s[0:1].upper() + s[1:length-1] + s[length-1:length].upper()

print(s)
