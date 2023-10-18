num = [21,34,52,12]
print("Before append: ",num)
num.append(65)
print("After append: ",num)

num = [1,3,5]
even_extend = [4,8,10]
num.extend(even_extend)
print("After extend:",num)

#insert in list
num = [10,20,30]
num.insert(1,40)
print(num)

#insert2
num = ["Language","Python","C++"]
num[2] = 'C'
print(num)

#delete element
num = ["Python","Java","C++","C","Swift"]
del num[1]
print(num)

#delete more than one
num = ["Python","Java","C++","C","Swift"]
del num[1:4]
print(num)