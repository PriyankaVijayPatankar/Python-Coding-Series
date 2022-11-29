# Day 7
#  Write a program to find Number of days in a given month of a given year

month = int(input("Enter a month number: "))
if 1<month>12:
    print("Invalid input. Month number should be between 1 and 12.")

else:
    year = int(input("Enter a year: "))
    
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        print("Number of days is 31")

    elif ((year%4==0 and year%100!=0) or (year%400==0) and (month==2)):
        print("Number of days is 29")

    elif month==2:
        print("Number of days is 28")

    else:
        print("Number of days is 30")
