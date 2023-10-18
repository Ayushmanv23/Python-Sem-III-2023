#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     25-09-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Calculator
a = int(input("Enter the first integer value:"))
b = int(input("Enter the second integer value:"))
print("SELECT OPERATION")
c = str(input("1. Add , 2.Sub, 3. Mul, 4.Modulo, 5.Div, 6.Factorial "))

if(c == "1"):
    print(a+b)
elif(c == "2"):
        print(a-b)
elif(c == "3"):
    print(a*b)
elif(c == "4"):
    print(a%b)

elif(c == "5"):
    print(a/b)
elif(c == "6"):

else:
    fac = int(input("Enter no whose factorial you want:"))
    if(c == "Factorial"):
     f = 1;
     for i in range(1,fac):
        f+= f*i;
     print(f)




'''#if else statement
a = int(input("Enter any integer number:"))
if(a>10):
    print("Number is greater than 10.")
elif(a>=10):
    print("Number is equal to 10.")
else:
    print("Number is smaller than 10.")



#even odd.
a = int(input("Enter any integer number:"))
if(a%2 == 0):
    print(a,"is Even.")
else:
    print(a,"is Odd.")'''



