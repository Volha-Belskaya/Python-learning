#calculator version 1


what = input('What do you do? (+, -):')

a = float( input('Enter first number:')) #добавить float, потому что input возвращает строку
b = float( input('Enter second number:'))

if what == '+':
    c = a + b
    print('Result:' + str(c)) #добавить str, чтобы привести переменную к типу float

elif what == '-':
    c = a - b
    print('Result:' + str(c))

else:
    print('Error')



       