# Day 20
# Write a program to identify if the number is prime number or not

num = int(input("Enter a number: "))

for i in range(2,int(num//2)+1):
	if num%i==0:
		print("The number is not a prime number")
		break
else:
	print("The input number is a prime number")

