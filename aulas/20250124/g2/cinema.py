lugares = []

for i in range(3):
    lugares.append([False] * 4)

# vender os ingressos
for i in range(12):
    # perguntar o lugar (linha e coluna)
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    # verificar se o lugar está disponível
    if lugares[linha][coluna] == False:
        # ocupar o lugar
        lugares[linha][coluna] = True
        # informar que deu certo
        print('vendido com sucesso!')
    else:
        # informar que deu errado
        print('O lugar escolhido não está disponível')


# calcular e informar quantos lugares foram vendidos com sucesso!
qtd = 0
for i in range(3):
    for j in range(4):
        if lugares[i][j] == True:
            qtd += 1

print(qtd)
    
