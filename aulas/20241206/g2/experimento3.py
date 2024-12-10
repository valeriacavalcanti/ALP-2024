import random

matriz = []

# declarar uma matriz 6 x 4
for i in range(6):
    matriz.append([0] * 4)

# exibir todos as posições dessa matriz
for i in range(6):
    for j in range(4):
        print(i, j)

# preencher a matriz com valores aleatórios entre 1 e 10
for i in range(6):
    for j in range(4):
        matriz[i][j] = random.randint(1, 10)

# exibir todos os elementos da matriz
print(matriz)

# exibir as linhas da matriz
for i in range(6):
    print(matriz[i])

# exibir cada elemento da matriz
for i in range(6):
    for j in range(4):
        #print(i, j, '-', matriz[i][j])
        print(f'Linha: {i} - Coluna: {j} - Valor: {matriz[i][j]}')
