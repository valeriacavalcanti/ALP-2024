palavra = input('Digite uma palavra: ')
n = int(input('Digite o valor de n: '))

for i in range(len(palavra)):
    print(palavra[i], end=' ' * n)
