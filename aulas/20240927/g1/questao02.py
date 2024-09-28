qtd_validas = 0
soma_validas = 0
qtd_erradas = 0

for i in range(40):
    nota = int(input('Nota: '))
    
    # verificar se a nota é válida
    if (nota >= 0) and (nota <= 100):
        qtd_validas += 1
        soma_validas += nota
    else:
        # verificar se a nota é errada
        if (nota < 0):
            qtd_erradas = qtd_erradas + 1

    
# fim do for!

if (qtd_validas > 0):
    media_validas = soma_validas / qtd_validas
    print(f'Média das notas válidas: {media_validas}')
else:
    print('Nenhuma nota válida informada')
    
print(f'Quantidade de notas erradas: {qtd_erradas}')
