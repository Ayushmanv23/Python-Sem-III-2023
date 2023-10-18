#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     08-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list = [10,11.4,'Python',23,64]
length = len(list)
while(1):
    print("**** List_Iteration ****")
    print('1. By using loop (Variable)')
    print('2. By using loop (Range)')
    print('3. By using while loop')
    print('4. By using list Comprehension')
    print('5. By using Enumeration')
    print('6. Exit')
    v = int(input("Enter your choice:"))
    if(v == 1):
        for i in list:
            print(i)

    elif(v == 2):
        for i in range(0,5):
            print(list[i])

    elif(v == 3):
        i=0
        while(i<length):
            print(list[i])
            i+=1

    elif(v == 4):
        [print(i) for i in list]

    elif(v == 5):
        for i,val, in enumerate(list):
            print(i,",",val)

    else:
        exit







Enter your choice:1
Enter your choice:2
Enter your choice:3
Enter your choice:4
10
11.4
Python
23
64

Enter your choice:5
0 , 10
1 , 11.4
2 , Python
3 , 23
4 , 64






