def greetings_function(name): #Default type of argument will always be string
    print('Welcome',name) #indentation important

greetings_function('Adeeb')


def multi_greet(*names): #send any number of parameters
    print('Welcome members :',names)
    return len(names)

print('The length is ', multi_greet('John','Tom','Tim'))

