import random

numeros = []

for i in range(40):
    numeros.append(random.randint(0,100))

menor = numeros[0]
maior = numeros[0]

for i in range(1,40):
    if numeros[i] < menor:
        menor = numeros[i]

    if numeros[i] > maior:
        maior = numeros[i]

#print(numeros)

print(menor, maior)

print(min(numeros), max(numeros))
