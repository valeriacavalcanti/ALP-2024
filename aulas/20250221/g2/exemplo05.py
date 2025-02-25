import funcoes

# PROGRAMA PRINCIPAL

frase = input('Digite uma frase: ')

qtd_digitos = funcoes.contar_simbolos_numericos(frase)
qtd_vogais = funcoes.contar_vogais(frase)
qtd_palavras = funcoes.contar_palavras(frase)

print(f'Quantidade de símbolos numéricos = {qtd_digitos}')
print(f'Quantidade de vogais = {qtd_vogais}')
print(f'Quantidade de palavras = {qtd_palavras}')

