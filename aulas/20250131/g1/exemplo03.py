simbolo = input('Símbolo: ')
codigo = ord(simbolo)

if (codigo >= 48) and (codigo <= 57):
    print('Símbolo numérico')
else:
    if (codigo >= 65) and (codigo <= 90):
        print('símbolo - letras maiúsculas')
    else:
        if (codigo >= 97) and (codigo <= 122):
            print('símbolo - letras minúsculas')
        else:
            print('Símbolo especial')
