# Day 25
# Write a program to find area of a circle

rad = int(input("Enter the radius of circle: "))

if rad>=0:
    area = 3.142 * (rad ** 2)
    print("Area of circle with radius",rad,"units is",area,"square units")

else:
    print("Invalid input")