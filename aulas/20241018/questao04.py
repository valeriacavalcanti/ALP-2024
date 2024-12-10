soma = 0
qtd = 0

numero = int(input('Número: '))
while (numero % 10 == 0):
    qtd += 1
    soma += numero
    numero = int(input('Número: '))

if (qtd > 0):
    print(f'Soma dos múltiplos: {soma}')
else:
    print('Nenhum múltiplo de 10 foi informado')
