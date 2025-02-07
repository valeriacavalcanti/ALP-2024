# listao = [[10,20,30,40], [50,60,70,80], [90,100,110,120]]

listao = []
listao.append([10,20,30,40])
listao.append([50,60,70,80])
listao.append([90,100,110,120])

print(listao)
# alterar todos os elementos do listão para 0 (zero)

for i in range(3):
    for j in range(4):
        listao[i][j] = 0

print(listao)
