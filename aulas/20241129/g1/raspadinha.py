import random

premios = [0] * 17
marcacao = [True] * 17

# Gerar cada pontuação
for i in range(17):
    premios[i] = random.randint(1,10)


for i in range(17):
    #print(marcacao)

    # exibir apenas as opções disponíveis (True)
    for j in range(17):
        if (marcacao[j] == True):
            print(j, end=' ')

    posicao = int(input('- Escolha seu prêmio: '))
    
    if (posicao >= 0 and posicao <= 16 and marcacao[posicao] == True):
        print(f'Premio: {premios[posicao]} pontos.')
        marcacao[posicao] = False
    else:
        print('Não está disponível')

print(marcacao)
print(premios)