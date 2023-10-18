#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     06-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------

Lab experiment-2


#Iteration on string through loop ( By variable, By range)
list = [10,10.4,'Hello',53,'@']
length=len(list)
for i in list:
    print(i)                       #by Variable

list = [10,10.4,'Hello',53,'@']
length=len(list)
for i in range(length):
    print(list[i])

list = [10,10.4,'Hello',53,'@']     #by Range
length=len(list)
for i in range(0,5):
    print(list[i])


#By while loop
list = [10,10.4,'Hello',53,'@']
length=len(list)
i=0
while(i<length):
  print(list[i])
  i+=1



'''#choose the word to extract
a = 'Welcome to Python World'
c = str(input('Enter the word you want to extract:'))

if(c == 'Welcome'):
    print(a[0:7])
elif(c == 'to'):
    print(a[8:10])
elif(c == 'Python'):
    print(a[11:17])
elif(c == 'World'):
    print(a[18:23])
else:
    print("Invalid choice.")'''



#using comprehension
list = [10,10.4,'Hello',53,'@']
[print(i) for i in list]

#using enumeration
list = [10,10.4,'Hello',53,'@']
length=len(list)
for i,val, in enumerate(list):
    print(i,",",val)
