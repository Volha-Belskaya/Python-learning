#calculator version 1


what = input('What do you do? (+, -):')

a = float( input('Enter first number:')) #�������� float, ������ ��� input ���������� ������
b = float( input('Enter second number:'))

if what == '+':
    c = a + b
    print('Result:' + str(c)) #�������� str, ����� �������� ���������� � ���� float

elif what == '-':
    c = a - b
    print('Result:' + str(c))

else:
    print('Error')



       