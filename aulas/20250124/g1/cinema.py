# declarar uma matriz 3 x 4
lugares = []
for i in range(3):
    lugares.append([False] * 4)


# ler os lugares das 12 pessoas
for i in range(4):
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if lugares[linha][coluna] == False:
        lugares[linha][coluna] = True
        print('vendido!')
    else:
        print('desculpe, esse lugar já foi vendido')


# exibir a quantidade de lugares vendidos com sucesso

qtd = 0
for i in range(3):
    for j in range(4):
        if lugares[i][j] == True:
            qtd += 1

print(qtd)
