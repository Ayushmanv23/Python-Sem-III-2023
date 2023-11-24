#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     31-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Choose from below:")
print("1. Celsius to fahrenheit")
print("2. Fahrenheit to celsius")
print("3. Exit")
n = int(input("Enter your choice:"))
if(n == 1):
    celsius = float(input("Enter the degree in Celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The fahrenheit degree is ",fahrenheit)
elif(n == 2):
    fahrenheit = float(input("Enter the degree in Fahrenheit:"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The Celsius degree is ",celsius)
else:
    print("Exit")