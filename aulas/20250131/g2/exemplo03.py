simbolo = input('Símbolo: ')
codigo = ord(simbolo)
binario = bin(codigo)

print(simbolo)
print(codigo)
print(binario)

if (codigo >= 48) and (codigo <= 57):
    print('Símbolo numérico')
else:
    if (codigo >= 65) and (codigo <= 90):
        print('Símbolo do alfabeto maiúsculo')
    else:
        if (codigo >= 97) and (codigo <= 122):
            print('Símbolo do alfabeto minúsculo')
        else:
            print('Caractere especial')
