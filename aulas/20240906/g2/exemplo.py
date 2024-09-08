soma = 0

qtd = int(input('Quantidade de alunos: '))

for i in range(qtd):
    media_aluno = int(input(f'Média do {i + 1}º aluno: '))
    soma = soma + media_aluno

print(soma)
media_turma = soma // qtd
bonus = media_turma * 0.1
print('Média da turma:', media_turma)
print('Bonus:', bonus)
