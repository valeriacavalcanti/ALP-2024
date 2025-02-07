numeros = [0] * 100
qtd = 0

for i in range(100):    
    numeros[i] = int(input('Número: '))
    if (numeros[i] >= 0 and numeros[i] <= 100):
        qtd += 1

for i in range(100):
    print(numeros[i])
    #if (numeros[i] >= 0 and numeros[i] <= 100):
    #    qtd += 1

print(qtd)
