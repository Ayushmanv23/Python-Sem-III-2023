#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     10-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Binary search
list = [1,2,3,4,5,6,7,8,9,10]
mid = len(list)//2
target = int(input("Enter the target element:"))
if(mid == target):
    print("Element found is",mid)
elif(target < mid):
    found = False
    for i in range(mid):
        if list[i] == target:
            print("Element found at index", i)
            found = True
            i-=1
            break
    if not found:
        print("Element not found.")
elif(target > mid):
    found = False
    for i in range(mid,len(list)):
        if list[i] == target:
            print("Element found at index", i)
            found = True
            break
    if not found:
        print("Element not found.")
