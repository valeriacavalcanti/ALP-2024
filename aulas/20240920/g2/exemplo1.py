import random

numero_aleatorio = random.randint(1, 20)
num = int(input('Número: '))

while (num != numero_aleatorio):
    print('eita')
    num = int(input('Número: '))

print('saiu')
