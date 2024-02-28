#Arrays or Lists
print('\n\n*********Lists*****')
countries  = ['UK' , 'Australia', 'US', 'India']
print(countries[2])
print(countries[1:3])
print(countries[2:])
print(type(countries))
countries[0] = 98
print(countries[-4])


#using a list constructor
list1= list((1,2,3,4,5))
print(list1)
list2= list((1,2,3,4,5, 4.5))
print(list1)
list1.extend(list2)
print(list1)
list1.append('Cherry')
print(list1)
list1.insert(2, 'Two.Five')
print(list1)
list1.remove(5)
print(list1)
list1.remove(5)
print(list1)
print(list1.count(3))
list1.clear() #will clear the list but keep the variable memory
print("This is list 1 : ",list1)
list2.sort()
print(list2)
list2.reverse()
print(list2)
list3 = list2.copy()
print(list3)
list3.pop()
print(list3)
list3.pop(2)
print(list3)
del list3[0] #will remove the variable memory too
print(list3)