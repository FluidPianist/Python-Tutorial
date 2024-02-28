try:
    x = int(input( 'Input an Integer: '))
    print(len(x))
except ValueError:
    print('Value not an Integer')
except Exception as e:
    print('Something went wrong')
    print(e)
else:
    print('Code Executed Successfully')
finally:
    print('Code Execution Fininshed')