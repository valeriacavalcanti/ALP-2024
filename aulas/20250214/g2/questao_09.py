"""
9. Escreva um programa para exibir todas as letras maiúsculas
   com respectivos códigos decimal e binário.
"""

cod_A = ord('A')
cod_Z = ord('Z')

for i in range(cod_A, cod_Z + 1):
    print(chr(i), i, bin(i))
