#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ayush
#
# Created:     08-10-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Practice code directory
d = {"Aryan":78,"Gagandeep":87,"Kunal":34,"Peeyush":10,"Ayushman":96}
for v in range(1,5):
     if(d.values(v) > d.values(v+1)):
      print(v)
     else:
      break






#Practice dictionary
'''my_dict = {"Name":"John","Age":30,"City":"Jammu"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())'''


'''d = {"Key1":1,"Key2":2,"Key3":3}
for k,v in d.items():
    print(k, v)'''



'''d = {'key1':1,'key2':2,'key3':3}
for k in d:
    print(k)
print(list(d))
print(type(list(d)))
while(1):
    print('**** DICTIONARY ITERATION ****')
    print('1.Through Dictionary keys')
    print('2.Through Dictionary values')
    print('3.Through Dictionary items')
    print('4.Exit')
    c=int(input('Enter Your Choice:'))
    if(c == 1):
        for k in d.keys():
            print(k)
        print(d.keys())
        print(type(d.keys()))
        print(list(d.keys()))
        print(type(list(d.keys())))
    elif(c == 2):
        for v in d.values():
            print(v)
        print(d. values())
        print(type(d.values()))
    elif(c == 3):
        for k, v in d.items():
            print('Keys=',k,'Values=',v)
        print(d.items())
        print(type(d.items()))
    elif(c == 4):
        break'''
