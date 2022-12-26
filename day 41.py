# Day 41
# Check if two strings match where one string contains wildcard characters

def match(s1,s2):
    a = len(s1)
    b = len(s2)
    if (a==0 and b==0):
        return True
    if (a>1 and s1[0]=='*') and b==0:
        return False
    if (a>1 and s1[0]=='?') or (a!=0 and b!=0 and s1[0]==s2[0]):
        return match(s1[1:],s2[1:])
    if (a!=0 and s1[0]=='*'):
        return match(s1[1:],s2) or match(s1,s2[1:])
    return False

s1 = input('Enter a string with wild characters: ')
s2 = input('Enter a string without wild characters: ')

if (match(s1,s2)):
    print("Yes they match")
else:
    print("No they don't match")