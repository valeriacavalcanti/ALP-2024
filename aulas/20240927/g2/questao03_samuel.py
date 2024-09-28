fatias_distribuidas = 0
clientes_felizes = 0

while (fatias_distribuidas < 10):
    fatias = int(input('Quantidade de fatias: '))
    fatias_distribuidas = fatias_distribuidas + fatias
    clientes_felizes = clientes_felizes + 1

print(f'Quantidade de clientes atendidos: {clientes_felizes}')
