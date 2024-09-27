qt_pessoas = int(input('Quantidade de pessoas: '))
soma = 0

for i in range(qt_pessoas):
    idade = int(input('Idade: '))
    soma = soma + idade

media = soma // qt_pessoas

print(f'Média do grupo: {media}')
