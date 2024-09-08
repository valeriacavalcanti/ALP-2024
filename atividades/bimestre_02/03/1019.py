tempo = int(input('Tempo total em segundos: '))

# 1h = 3600 segundos
horas = tempo // 3600

tempo = tempo % 3600

# 1 min = 60 segundos
minutos = tempo // 60

segundos = tempo % 60

print(f'{horas}:{minutos}:{segundos}')
print(horas, minutos, segundos, sep=':')