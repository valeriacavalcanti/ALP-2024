l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

soma = l1 + l2 + l3
area = ((l1 + l2) * l3)/2

# Descobrir o maior lado
if (l1 > l2) and (l1 > l3):
    maior = l1
elif (l2 > l3):
    maior = l2
else:
    maior = l3

# Verificar se forma triangulo
demais_lados = soma - maior
if (maior < demais_lados):
    print(f'Perimetro = {soma:.1f}')
else:
    print(f'Area = {area:.1f}')