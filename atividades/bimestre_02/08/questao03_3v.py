# Condição de parada definida no Loop
# Ideia central: Substrair do estoque de fatias até acabar o estoque.

estoque = 10
clientes_atendidos = 0

while (estoque > 0):
    fatias = int(input('Quantidade de fatias: '))
    estoque = estoque - fatias
    clientes_atendidos = clientes_atendidos + 1

# Depois do while
print(f'Quantidade de clientes atendidos: {clientes_atendidos}')

# Extra: Verificando se o último cliente foi plenamente atendido, ou seja, recebeu todas as fatias que pediu.
if (estoque == 0):
    print('Todos os clientes foram plenamente atendidos.')
else:
    fatias_faltando = estoque * (-1)
    print(f'O último cliente não recebeu todas as fatias que pediu. Faltou(ram) {fatias_faltando}')