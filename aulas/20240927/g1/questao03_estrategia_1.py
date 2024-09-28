# estratégia 01

soma_fatias_entregues = 0
qtd_atendidos = 0

while True:
    fatias = int(input('Quantidade de fatias: '))
    soma_fatias_entregues = soma_fatias_entregues + fatias

    qtd_atendidos += 1

    if (soma_fatias_entregues >= 1000):
        break

# saiu

print(f'Quantidade de clientes antendidos: {qtd_atendidos}')
