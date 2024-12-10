import random

premios = [0] * 15
marcacao = [True] * 15

# preencher com valores aleatórios entre 1 de 10
for i in range(15):
    premios[i] = random.randint(1,10)

# ler os pedidos de cada pessoa
for i in range(15):
    # print(marcacao)

    # exibir as posições disponíveis (True)
    for j in range(15):
        if (marcacao[j] == True):
            print(j, end = ' ')

    # obter a posição do prêmio desejado
    posicao = int(input('Posição: '))

    # verificar se o prêmio está disponível
    if (marcacao[posicao] == True):
        marcacao[posicao] = False
        print(f'Prêmio: {premios[posicao]} pontos!')
    else:
        print('É uma pena! Prêmio indisponível!')