num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if (num1 == num2):
    print('São iguais')
else:
    if (num1 > num2):
        print(f'{num1} é o maior')
    else:
        print(f'{num2} é o maior')
