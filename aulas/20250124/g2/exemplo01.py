# declarar o listao
listao = [[10,20,30,40], [50,60,70,80], [90,100,110,120]]

# exibir o listao
print(listao)

# zerar o listao (alterar todos os elementos para zero)
for i in range(3):
    for j in range(4):
        listao[i][j] = 0

# exibir o listao
print(listao)
