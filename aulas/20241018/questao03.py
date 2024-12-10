qtd_quadrados = 0

for i in range(3):
    print(f'Figura geométrica {i + 1}')
    largura = int(input('Largura: '))
    altura = int(input('Altura: '))

    # verificar se a figura é um quadrado
    if (largura == altura):
        qtd_quadrados = qtd_quadrados + 1
        # qtd_quadrados += 1

print(f'Quantidade de quadrados: {qtd_quadrados}')
