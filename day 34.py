# Day 34
# Write a program to Remove brackets from an algebraic expression

s = input("Enter an algebraic expression: ")
s1 = ''

for i in s:
    if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
        pass
    else:
        s1 = s1 + i
print("The input expression without brackets is:",s1)