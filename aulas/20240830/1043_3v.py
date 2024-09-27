a = input('A: ')
a = float(a)

b = float(input('B: '))
c = float(input('C: '))

perimetro = a + b + c
area = ((a + b)*c)/2


# descobrir o maior lado

if (a > b) and (a > c):
    # a é o maior
    if (a < b + c):
        print(f'Perimetro: {perimetro:.1f}')
    else:     
        print(f'Area: {area:.1f}')
elif (b > c):
    # b é o maior
    if (b < a + c):
        print(f'Perimetro: {perimetro:.1f}')
    else:
        print(f'Area: {area:.1f}')
else:
    # c é o maior
    if (c < b + a):
        print(f'Perimetro: {perimetro:.1f}')
    else:
        print(f'Area: {area:.1f}')


