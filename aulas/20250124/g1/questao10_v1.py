import random

numeros = []

for i in range(40):
    numeros.append(random.randint(0,100))

#print(numeros)

maior = max(numeros)
menor = min(numeros)

print(menor, maior)
