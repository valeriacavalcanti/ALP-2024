misterio = []

misterio.append(8)
misterio.append(28.2)
misterio.append('IFPB')
misterio.append(True)
misterio.append([10,20,30,40])

for i in range(len(misterio)):
    print(i, misterio[i], type(misterio[i]))


# exibir os valores que estão na lista
# que está no índice 4 do mistério

for i in range(4):
    print(misterio[4][i])
