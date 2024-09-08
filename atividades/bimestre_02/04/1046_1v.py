hora_inicio = int(input('Hora inicio: '))
hora_fim = int(input('Hora fim: '))

if (hora_inicio >= hora_fim):
    d1 = 24 - hora_inicio
    d2 = hora_fim
    duracao = d1 + d2
else:
    duracao = hora_fim - hora_inicio

print(f'O JOGO DUROU {duracao} HORA(S)')