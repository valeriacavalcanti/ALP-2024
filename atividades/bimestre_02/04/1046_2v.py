hora_inicio = int(input('Hora inicio: '))
hora_fim = int(input('Hora fim: '))

if (hora_inicio >= hora_fim):
    duracao = 24 - hora_inicio + hora_fim
else:
    duracao = hora_fim - hora_inicio

print(f'O JOGO DUROU {duracao} HORA(S)')