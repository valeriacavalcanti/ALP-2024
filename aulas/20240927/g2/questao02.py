soma_validas = 0
qtd_validas = 0
qtd_erradas = 0

for i in range(4):
    nota = int(input('Nota: '))

    # verificar se é válida
    if (nota >= 0) and (nota <= 100):
        qtd_validas = qtd_validas + 1
        soma_validas = soma_validas + nota

    # verificar se é errada
    if (nota < 0):
        qtd_erradas += 1
        # qtd_erradas = qtd_erradas + 1

# fora do for

if (qtd_validas > 0):
    media_validas = soma_validas / qtd_validas
    print(f'Média das notas válidas é {media_validas:.0f}')
else:
    print('Não existe nota válida!')

print(f'Quantidade de notas erradas é {qtd_erradas}')
