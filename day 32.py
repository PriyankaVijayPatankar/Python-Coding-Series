# Day 32
# Write a Program to Remove vowels from a string

s = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
p = ''

for i in range(len(s)):
    if s[i] not in vowels:
        p = p + s[i]
        
print(p)
