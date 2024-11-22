# Código I

lista = []

while True:
    num = int(input('Número: '))
    if (num <= 0):
        break
    lista.append(num)

print(lista)

for i in range(len(lista)):
    print(lista[i])
