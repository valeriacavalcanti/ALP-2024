soma = 0
qt_pessoas = int(input('Quantidade de pessoas: '))

for i in range(qt_pessoas):
    idade = int(input('Idade: '))
    soma = soma + idade

media = soma // qt_pessoas

print(f'Média = {media}')
