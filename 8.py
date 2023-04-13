# leap year or not leap year
"""
condition of leap year
 year is divided  4 and 100 and if year is divided by 100 it should  be divisuble by 400 
"""
year = int(input("enter your year: "))

if year%4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")


# if (year%400 == 0) or(year%4 == 0 and year%100!=0):
#     print("Leap year")
# else:
#     print("Not leap year")