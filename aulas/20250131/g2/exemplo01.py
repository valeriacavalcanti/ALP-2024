nome = input('Digite seu nome: ')

for i in range(len(nome)):
    codigo = ord(nome[i])
    print(i, nome[i], type(nome[i]), codigo, bin(codigo))
