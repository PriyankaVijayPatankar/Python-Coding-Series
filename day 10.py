# Day 10 
# Get a number from the user and calculate the factorial and give it as the output.

num = int(input("Enter a number: "))
fact = 1

if num<0:
    print("Invalid input")
    
else:
    for i in range (1,num+1):
        fact = fact*i
    print("Factorial of",num,"is",fact)
