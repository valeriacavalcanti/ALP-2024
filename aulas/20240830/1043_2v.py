a = input('A: ')
a = float(a)

b = float(input('B: '))
c = float(input('C: '))


# descobrir o maior lado

if (a > b) and (a > c):
    # a é o maior
    if (a < b + c):
        perimetro = a + b + c
        print(f'Perimetro: {perimetro:.1f}')
    else:
        area = ((a + b)*c)/2
        print(f'Area: {area:.1f}')
elif (b > c):
    # b é o maior
    if (b < a + c):
        perimetro = a + b + c
        print(f'Perimetro: {perimetro:.1f}')
    else:
        area = ((a + b)*c)/2
        print(f'Area: {area:.1f}')
else:
    # c é o maior
    if (c < b + a):
        perimetro = a + b + c
        print(f'Perimetro: {perimetro:.1f}')
    else:
        area = ((a + b)*c)/2
        print(f'Area: {area:.1f}')


