# Partindo de um Loop infinito
# Ideia central: Somar as fatias distribuídas até atingir o limite.

fatias_distribuidas = 0
clientes_atendidos = 0

while True:
    fatias = int(input('Quantidade de fatias: '))
    fatias_distribuidas = fatias_distribuidas + fatias
    clientes_atendidos = clientes_atendidos + 1

    # encerrar o loop se as fatias já foram todas distribuídas
    if (fatias_distribuidas >= 10):
        break

# Depois do while
print(f'Quantidade de clientes atendidos: {clientes_atendidos}')

# Extra: Verificando se o último cliente foi plenamente atendido, ou seja, recebeu todas as fatias que pediu.
if (fatias_distribuidas == 10):
    print('Todos os clientes foram plenamente atendidos.')
else:
    fatias_faltando = fatias_distribuidas - 10
    print(f'O último cliente não recebeu todas as fatias que pediu. Faltou(aram) {fatias_faltando}')