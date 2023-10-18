#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ayushman Vohra
#
# Created:     05-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Options to perform on string:")
print("1. Count alphabet.")
print("2. Extract string.")
print("3. Check alphanumeric.")
c = int(input('Enter your choice:'))

if(c == 1):
    #string lab-2 experiment (i)
    a = "Welcome to Python World"
    c = 0
    for i in a:
        if  i.isalpha():
         c+=1
    print(c)

elif(c == 2):
    #extract string (ii)
    a = 'Welcome to the Python World'
    print(a[15:21])

elif(c == 3):
    #string isalnum (iii)
    a = input("Enter string:")
    if(a.isalnum()):
        print("Given string is Alphanumeric.")
    else:
        print("Given string is not Alphanumeric")

else:
    print("Invalid choice.")



