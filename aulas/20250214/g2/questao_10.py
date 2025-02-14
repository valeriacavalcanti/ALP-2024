"""
10.Escreva um programa para ler uma frase e EXIBIR
   essa frase trocando as vogais por “*” (asterisco).
"""

frase = input('Frase: ')

vogais = 'aeiouAEIOU'

for i in range(len(frase)):
    if (frase[i] in vogais):
        print('*', end = '')
    else:
        print(frase[i], end = '')
