# Day 1

# Write a program to identify if the character is a vowel or consonant.

inp=input(“Enter any alphabet: )
if((inp>='a' and inp<='z') or (inp>='A' and inp<='Z') ):
    if (inp=='a' or inp=='e' or inp=='i' or inp=='o' or inp=='u' or inp=='A'or inp=='E' or inp=='I' or   inp=='O' or inp=='U' ):
        print("The input alphabet is a Vowel")
    else:
        print("The input alphabet is a Consonant")
else:
    print("Invalid Input")
