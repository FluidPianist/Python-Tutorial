print("hello World\nwelcome",100)

#print function
name = 'Adeeb'
age = 24
print(name,'is my name')
print('Hey',name+'!!')
#print('My age is '+age); error
print('My age is',age)

#string functions

print('\n\n*********Strings*****')
print(name.islower())
print(name.lower())
print(len(name))
print(name.index('b'))
print(name.replace('d' , 'D')) #can be used for strings too besides characters

#numbers
print('\n\n*********Number*****')
print(78 / 22.0989)
print(20/6)
print(20%6)
number = 55
numberString = str(number)
print('This is String : '+numberString)
print(abs(-5))
print(max(4 , 3, 5, 2))
print(min(4 , 3 ,2 ,1 ))
print(round(3.2))
print(round(3.5))
print(bin(5))

#From Math file import all 
from math import *
print(sqrt(100))

''' multi Line comment
Taking Inputs
name1 = input("Enter your name: ")
age = int(input('Enter your age'))
print('Hi '+name1+' of age',age)
'''