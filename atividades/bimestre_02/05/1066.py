par = 0
pos = 0
neg = 0

for i in range(5):
    num = int(input("Digite um número: "))
    if (num %2 == 0):
        par = par + 1
    if (num > 0):
        pos = pos + 1
    elif (num < 0):
        neg = neg + 1

print(par, 'valor(es) par(es)')
print(5-par, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s))')