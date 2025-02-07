palavra = input('Digite uma palavra: ')
tamanho = len(palavra)

for i in range(tamanho):
    simbolo = palavra[i]
    codigo_decimal = ord(simbolo)
    codigo_binario = bin(codigo_decimal)
    print(simbolo, codigo_decimal, codigo_binario)
