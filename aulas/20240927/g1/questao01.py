qtd_10_50 = 0
qtd_0 = 0
qtd_validos = 0

valor = float(input('Valor: '))
while (valor >= 0):
    qtd_validos += 1
    if (valor >= 10) and (valor <= 50):
        qtd_10_50 = qtd_10_50 + 1

    if (valor == 0):
        qtd_0 += 1
    
    valor = float(input('Valor: '))

# aqui!!!!
print(f'Quantidade entre 10 e 50 = {qtd_10_50}')
print(f'Quantidade "de grátis" = {qtd_0}')
print(f'Quantidade de valores válidos = {qtd_validos}')
