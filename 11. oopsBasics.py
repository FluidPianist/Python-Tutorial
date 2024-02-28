class Person: 
    id = 5
    #constructor 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

p1 = Person('Adeeb', 24)
print(p1)
print(p1.id)
print(p1.name)
print(p1.age)
del p1

#Inheriting from Person Class
class Employee(Person):
    pass #write pass to make the class or function empty

p2 = Employee('Adeeb',24)
del p2