# Day 8
#  Write a program to find roots of a quadratic equation

a = int(input("Enter the value of a i.e coefficient of x: "))
b = int(input("\nEnter the value of b i.e coefficient of y: "))
c = int(input("\nEnter the value of c i.e constant: "))

root1 = (-b+((b*b)-4*a*c)**(1/2))/2*a
root2 = (-b-((b*b)-4*a*c)**(1/2))/2*a

if (root1 == root2):
    print("\nRoots are equal\nRoot 1 = Root 2 =",root1)
else:
    print("\nRoots of the quadratic equation are:\n",root1,"and",root2)
