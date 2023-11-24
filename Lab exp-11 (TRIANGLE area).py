#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     20-11-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#function to call collection
'''def collection(list):
    for ind,var in enumerate(list):
        print(ind,"The value is:",var)
    print()

list = [1,2,3,4,5]
collection(list)'''



#Lab 11 experiment
def is_rat(a,b,c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Yes, it's a right-angled triangle.")
    else:
        print("No, it's not a right-angled triangle.")

def cal_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("Area:", area)

a = float(input("Enter the value of side a:"))
b = float(input("Enter the value of side b:"))
c = float(input("Enter the value of side c:"))

is_rat(a,b,c)
cal_area(a,b,c)