l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

# Descobrir se forma triângulo
# Cada lado deve ser menor que a soma dos outros dois
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    perimetro = soma = l1 + l2 + l3
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((l1 + l2) * l3)/2
    print(f'Area = {area:.1f}')
