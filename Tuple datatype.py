#del element from range
list = [2,4,7,8,5]
del list[0:2]
print(list)

#remove element by its name.
list = ['Python','Java','C','C++','Swift']
list.remove('Java')
print(list)

#practice
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
list.append(11)
list.insert(0,0)
list.remove(5)
print(list)

#hello
my_tuple = ()
print(my_tuple)


my_tuple = (1,"Hello",3.4)
print(my_tuple)

my_tuple = ("mouse",[8,4,6],(1,2,3))
print(my_tuple)

var1 = ("Hello")
var2 = ("Hello",)
print(type(var1))
print(type(var2))

#tuple manipulation
#visit elements using loop
languages = ('Python','Swift','C','C++')
for language in languages:
    print(language)


#existance of item
languages = ('Python','Swift','C++')
print('C' in languages)
print('Python' in languages)