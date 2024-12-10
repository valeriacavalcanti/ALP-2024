misterio = []

misterio.append(6)
misterio.append(32.8)
misterio.append('IFPB')
misterio.append(True)
misterio.append([10,20,30,40])

for i in range(len(misterio)):
    print(i, type(misterio[i]), misterio[i])

# exibir os elementos que estão na sub-lista
for i in range(len(misterio[4])):
    print(i, misterio[4][i])
