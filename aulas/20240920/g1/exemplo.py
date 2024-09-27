import random

numero_aleatorio = random.randint(1 ,10)

num = int(input('Número: '))

while (num != numero_aleatorio):
    print('não é esse')
    num = int(input('Número: '))

print(num, numero_aleatorio)
