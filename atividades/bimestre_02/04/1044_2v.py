n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

# Ordenar
if (n1 > n2):
    n1, n2 = n2, n1

if (n2 % n1 == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')