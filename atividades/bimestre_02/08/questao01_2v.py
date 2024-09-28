# Partindo de um Loop Infinito

qtd_entre_10_50 = 0
qtd_gratis = 0

while True:
    valor = float(input('Valor: '))

    # encerrar o loop se o número for negativo
    if (valor < 0):
        break

    # verificar se está entre 10 e 50
    if (valor >= 10) and (valor <= 50):
        qtd_entre_10_50 = qtd_entre_10_50 + 1

    # verificar se o valor é zero (de graca)
    if (valor == 0):
        qtd_gratis = qtd_gratis + 1
    

# Depois do while

print(f'Quantidade de valores entre 10 e 50 = {qtd_entre_10_50}')
print(f'Quantidade de valores zero (grátis) = {qtd_gratis}')