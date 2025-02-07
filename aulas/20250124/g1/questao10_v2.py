import random

numeros = []

menor = 101
maior = -1

for i in range(40):
    numeros.append(random.randint(0,100))

for i in range(40):
    if numeros[i] < menor:
        menor = numeros[i]

    if numeros[i] > maior:
        maior = numeros[i]

#print(numeros)

print(menor, maior)

print(min(numeros), max(numeros))
