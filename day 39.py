# Day 39
# Write a Program to check if two strings are Anagram or not

Str1 = input("Enter a string: ")
Str2 = input("Enter another string: ")

if len(Str1)!=len(Str2):
    print('Not anagram')

else:
    Str1 = sorted(Str1)
    Str2 = sorted(Str2)
    
    if Str1==Str2:
        print('The input strings are anagram')
        
    else:
         print('The input strings are not anagram')
