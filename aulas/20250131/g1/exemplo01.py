nome_binario = ''

nome = input('Nome: ')
print(nome)

for i in range(len(nome)):
    codigo = ord(nome[i])
    print(i, nome[i], codigo, bin(codigo))
    nome_binario += bin(codigo)

print(nome_binario)
