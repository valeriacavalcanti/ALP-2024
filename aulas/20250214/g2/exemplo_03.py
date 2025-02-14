"""
  programa para exibir todas as posições onde inicia um pastel
"""

frase = "eu adoro pastel chocolate pastel carne pastel frango"

start = 0
stop = len(frase)

posicao = frase.find('pastel', start, stop)

while (posicao >= 0):
    print(f'Encontrei na posicao: {posicao}')
    start = posicao + 1
    posicao = frase.find('pastel', start, stop)



