a = input('A: ')
a = float(a)

b = float(input('B: '))

c = float(input('C: '))


# descobrir o maior lado

if (a > b) and (a > c):
    # a é o maior
    maior = a
    soma = b + c
elif (b > c):
    # b é o maior
    maior = b
    soma = a + c
else:
    # c é o maior
    maior = c
    soma = a + b

# verificar se forma triângulo
if (maior < soma):
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a + b)*c)/2
    print(f'Area = {area:.1f}')

    
