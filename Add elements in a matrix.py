#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     13-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Matrix = [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
a=0
for r in Matrix:
    for c in r:
        print(c,end=" ")
    print()
for r in Matrix:
    for c in r:
        a+=c
print()
print("The sum is",a)