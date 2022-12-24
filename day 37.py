# Day 37
# Write a program to calculate the Frequency of characters in a string

Str = input("Enter a string: ")
freq = 0

for i in range(0,len(Str)):
    Character = Str[i]
    freq = Str.count(Character)
    print(str(freq) + ' is the frequency of '+Character)
