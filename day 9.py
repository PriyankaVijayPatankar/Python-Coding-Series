# Day 9 
# Write a program to find Number of digits in an integer

inp = input("Enter a number: ")
count = 0

for i in inp:
    count=count+1
    
print("Number of digits in the input number are:", count)


# using len()
# print("Number of digits in the input number are:", len(str(inp))) 
