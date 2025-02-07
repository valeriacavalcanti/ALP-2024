simbolo = input('Símbolo: ')

if (simbolo >= '0') and (simbolo <= '9'):
    print('Símbolo numérico')
else:
    if (simbolo >= 'A') and (simbolo <= 'Z'):
        print('símbolo - letras maiúsculas')
    else:
        if (simbolo >= 'a') and (simbolo <= 'z'):
            print('símbolo - letras minúsculas')
        else:
            print('Símbolo especial')
