s1 = 'ifpb'
s2 = 'IFPB'

for i in range(4):
    codigo1 = ord(s1[i])
    codigo2 = ord(s2[i])
    #print(i, s1[i], s2[i])
    print(i, codigo1, codigo2, codigo1 - codigo2)
