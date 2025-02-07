numeros = [0] * 100
soma = 0

for i in range(100):    
    numeros[i] = int(input('Número: '))
    soma = soma + numeros[i]

for i in range(100):
    print(numeros[i])
    # soma = soma + numeros[i]

print(soma)
