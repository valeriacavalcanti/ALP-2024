estoque = 10
clientes_felizes = 0

while (estoque > 0):
    fatias = int(input('Quantidade de fatias: '))
    estoque = estoque - fatias
    clientes_felizes = clientes_felizes + 1

print(f'Quantidade de clientes atendidos: {clientes_felizes}')
