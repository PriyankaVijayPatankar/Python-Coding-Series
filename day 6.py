# Day 6
# Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

inpx = int(input("Enter x coordinate: "))
inpy = int(input("Enter y coordinate: "))

if inpx>0:
    if inpy>0:
        print("The input point lies in First Quadrant")
    elif inpy<0:
        print("The input point lies in Fourth Quadrant")
    elif inpy==0:
        print("The input point lies on positive X-axis")
        
elif inpx<0:
    if inpy>0:
        print("The input point lies in Second Quadrant")
    elif inpy<0:
        print("The input point lies in Third Quadrant")
    elif inpy==0:
        print("The input point lies on negative X-axis")
        
elif inpx==0:
    if inpy>0:
        print("The input point lies on positive Y-axis")
    elif inpy<0:
        print("The input point lies on negative Y-axis")
    elif inpy==0:
        print("The input point lies on the origin")
