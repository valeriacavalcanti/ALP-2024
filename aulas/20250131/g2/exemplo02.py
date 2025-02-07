st1 = 'IFPB'
st2 = 'ifpb'

for i in range(4):
    codigo1 = ord(st1[i])
    codigo2 = ord(st2[i])
    print(i, st1[i], st2[i], codigo1, codigo2, codigo2 - codigo1)
