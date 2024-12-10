import random

# matriz vazia
matriz = []

# inserir 3 linhas, todas com 4 elementos (zero)
for i in range(3):
    matriz.append([0] * 4)

# exibir a matriz completa
print(matriz)

# exibir cada linha da matriz
for i in range(3):
    print(matriz[i])

# exibir cada elemento de cada linha da matriz
for i in range(3): # iterar as linhas
    for j in range(4): # iterar as colunas de CADA linha
        print(i,j,matriz[i][j])


# preencher a matriz com valores aleatórios entre 0 e 1
for i in range(3):
    for j in range(4):
        matriz[i][j] = random.randint(0,1)

# exibir cada linha matriz
for i in range(3):
    print(matriz[i])

