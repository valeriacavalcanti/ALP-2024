qt_aprovados = 0

for i in range(10):
    nota = int(input(f'Nota {i + 1}:'))
    if (nota >= 70):
        qt_aprovados = qt_aprovados + 1

print(f'Quantidade de aprovados: {qt_aprovados}')
    
