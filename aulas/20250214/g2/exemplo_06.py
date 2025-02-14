"""
  programa para calcular a quantidade de palavras.
"""

frase = "eu     adoro pastel     chocolate PASTEL    carne pASTel frango"
#qtd = frase.count(' ') + 1
qtd = len(frase.split())

print(frase)
print(qtd)


frase = "eu quero bolo com bolo chocolate e bolo muito bolo quero"
lista = frase.split('bolo')
print(lista)


