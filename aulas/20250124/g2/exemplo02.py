m1 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

m2 = [[0]*4, [0]*4, [0]*4]

m3 = [[0]*4]*3

m4 = []
for i in range(3):
    m4.append([0]*4)

print(m1)
print(m2)
print(m3)
print(m4)

m1[0][0] = 1
m2[0][0] = 2
m3[0][0] = 3
m4[0][0] = 4

print(m1)
print(m2)
print(m3)
print(m4)
