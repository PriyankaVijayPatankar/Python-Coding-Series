# Day 11
# Write a program to find Fibonacci series up to n

n = int(input("Enter the number of terms: "))
 
f0 = 0
f1 = 1
count = 0
print("Fibonacci series:")
 
while count < n:
    print(f0)
    new = f0 + f1
    f0 = f1
    f1 = new
    count = count + 1
