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

#conversion (Binary)
a = int(input("Enter any number for binary:"))
b = bin(a)
print(b)

#conversion(octal)
a = int(input("Enter any number for octal:"))
b = oct(a)
print(b)

#conversion(Hexadecimal)
a = int(input("Enter any number for hexa:"))
b = hex(a)
print(b)

#conversion (Explicit type conversion)
a = str(input("Enter string input for explicit:"))
b = float(a)
print(b)