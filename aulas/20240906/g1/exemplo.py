soma = 0

qtd = int(input('Quantidade de pessoas: '))

for i in range(qtd):
    qtd_chocolate = int(input(f'Chocolates da {i + 1}º pessoa: '))
    soma = soma + qtd_chocolate

print(f'Fabrizia vai comprar {soma} chocolates!')
