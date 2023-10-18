#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     29-09-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def prime(x,y):
    p=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i%j==0:
                    break
                else:
                    p.append[i]
    return p

x=2
y=14
lst=prime(x,y)
if len(lst)==0:
    print("there is no primes")
else:
    print(lst)