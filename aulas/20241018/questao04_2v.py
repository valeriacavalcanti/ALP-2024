soma = 0
qtd = 0

while True:
    numero = int(input('Número: '))

    if (numero % 10 != 0):
        break
    
    qtd += 1
    soma += numero
    

if (qtd > 0):
    print(f'Soma dos múltiplos: {soma}')
else:
    print('Nenhum múltiplo de 10 foi informado')
