qt_aprovados = 0
soma_aprovados = 0

for i in range(4):
    nota = int(input('Nota: '))

    if (nota >= 70):
        qt_aprovados = qt_aprovados + 1
        soma_aprovados = soma_aprovados + nota

if (qt_aprovados == 0):
    print('Ninguém passou

print(f'{qt_aprovados} pessoas estão aprovadas.')
media_aprovados = soma_aprovados / qt_aprovados
print(media_aprovados)
