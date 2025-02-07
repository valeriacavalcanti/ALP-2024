simbolo = input('Símbolo: ')
codigo = ord(simbolo)
binario = bin(codigo)

print(simbolo)
print(codigo)
print(binario)

if (simbolo >= '0') and (simbolo <= '9'):
    print('Símbolo numérico')
else:
    if (simbolo >= 'A') and (simbolo <= 'Z'):
        print('Símbolo do alfabeto maiúsculo')
    else:
        if (simbolo >= 'a') and (simbolo <= 'z'):
            print('Símbolo do alfabeto minúsculo')
        else:
            print('Caractere especial')
