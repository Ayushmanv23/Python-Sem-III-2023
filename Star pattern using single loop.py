#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     27-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Diamond with blank line
'''r = int(input("Enter the number of rows: "))
for i in range(1,r+1):
    print(" "*(r-i),"* "*i)
for i in range(r):
        if i!=0:
            if i==1:
                print(" ")
            else:
                print(" "*i,"* "*(r-i))'''




#Diamond star pattern
'''n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i),"* "*i)'''



#pyramid
'''n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)'''


#upside down pyramid
'''n = int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    print(" "*(n-i),"* "*i)'''






#Right sided triangle star pattern
n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()





#Left sided star pattern
'''for row in range(0,6):
    print(" *"*row)'''
