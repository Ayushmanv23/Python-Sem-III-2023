#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ayush
#
# Created:     13-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Lab-5 (Reverse the kth row)
M =      [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
for r in M:
    for c in r:
        print(c,end=" ")
    print()
kth = int(input("Enter the row you want to reverse:"))
res =[]
for idx, ele in enumerate(M):
    if(idx + 1) % kth == 0:
        res.append(list(reve))








'''#add diagonal ele
M =      [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
sum=0
for r in range(0,len(M)):
    for c in range(0,len(M[r])):
        if(r == c):
            sum+=M[r][c]
print(sum)'''




'''#column add
M =      [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
sum=0
for r in M:
    for c,e in enumerate(r):
        if(c == 3):
            sum+=e
print(sum)'''




'''#add even index elements
M = [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
sum=0
for r in M:
    for c in r:
        if(c%2 != 0):
            sum+=c
print("The sum of element at even is",sum)'''


'''#add enumerate
M =      [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
sum=0
for r in M:
    for i,c in enumerate(r):
        if(i%2 == 0):
            sum+=c
print(sum)'''





'''#add 3rd row
M =      [[1,2,3,4],#----0
          [5,6,7,8],#----1
          [9,10,11,12],#----2
          [13,14,15,16]#----3
         ]
a=0
for c in M[1]:
    a+=c
print()
print("The sum of elements in Row 2 is",a)'''




'''#even no. add
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
        if(c%2 == 0):
            a+=c
print()
print("The sum of the even numbers is",a)'''




'''#odd no. add
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
        if(c%2 != 0):
            a+=c
print()
print("The sum of the even numbers is",a)'''