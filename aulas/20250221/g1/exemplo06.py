import funcoes

'''
    Programa para ler um texto, calcular e exibir:
        - Quantidade de vogais;
        - Quantidade de letras maiúsculas
'''

# PROGRAMA PRINCIPAL

frase = input('Digite uma frase: ')

qtd_vogais = funcoes.quantidade_vogais(frase)
qtd_letras_maiusculas = funcoes.quantidade_letras_maiusculas(frase)
qtd_numeros = funcoes.quantidade_digitos_numericos(frase)

funcoes.simbolos_distintos(frase)

print(f'Quantidade vogais: {qtd_vogais}')
print(f'Quantidade de letras maiúsculas: {qtd_letras_maiusculas}')
print(f'Quantidade de dígitos numéricos: {qtd_numeros}')
