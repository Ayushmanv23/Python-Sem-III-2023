#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     09-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Linear search
list = [1, 3, 5, 7, 8, 9, 10, 12]
x = int(input("Enter the target element:"))
found = False
for i in range(len(list)):
    if list[i] == x:
        print("Element found at index", i)
        found = True
        break

if not found:

    print("Element not found.")
