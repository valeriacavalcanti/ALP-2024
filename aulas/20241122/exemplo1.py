# Código I

lista = []

num = int(input('Número: '))
while (num > 0):
    lista.append(num)
    num = int(input('Número: '))

print(lista)

for i in range(len(lista)):
    print(lista[i])
