# Day 18
# Write a program to Add two fractions

# Get the values for numerator and denominator of two fractions, then add that fractions. Consider the following format

# x3/y3 = (x1/y1) + (x2/y2)

# here x3 = (x1*y2) + (x2*y1) and y3 = (y1*y2)


def gcd(a, b):
	if (a == 0):
		return b
	return gcd(b % a, a)

def lowest(y3, x3):
	cf = gcd(x3, y3)
	y3 = int(y3 / cf)
	x3 = int(x3 / cf)
	print(x3, "/", y3)

def addFraction(x1, y1, x2, y2):
	y3 = gcd(y1, y2)
	y3 = (y1 * y2) / y3
	x3 = ((x1) * (y3 / y1) + (x2) * (y3 / y2))
	lowest(y3, x3)

# Driver Code
x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of x2: "))

x2 = int(input("Enter the value of y1: "))
y2 = int(input("Enter the value of y2: "))

print(x1, "/", y1, " + ", x2, "/",y2,"equals ", end="")

addFraction(x1, y1, x2, y2)