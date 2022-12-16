# Day 31
# Write a Program to Toggle each character in a string

s = input("Enter a string: ")
s1 = ""
for i in range(len(s)):
    if(s[i]>='a' and s[i]<='z'):
        s1=s1+chr((ord(s[i])-32))
    elif(s[i]>='A' and s[i]<='Z'):
        s1=s1+chr((ord(s[i])+32))
    else:
        s1=s1+s[i]
print("After toggling case: ",s1)