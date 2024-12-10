# medidas da caixa

print('Medidas da caixa')
altura_caixa = int(input('Altura: '))
largura_caixa = int(input('Largura: '))
profundidade_caixa = int(input('Profundidade: '))

print('Medidas do presente')
altura_presente = int(input('Altura: '))
largura_presente = int(input('Largura: '))
profundidade_presente = int(input('Profundidade: '))

# verificar se o presente cabe na caixa

if ((altura_presente + 1 <= altura_caixa) and
    (largura_presente + 1 <= largura_caixa) and
    (profundidade_presente + 1 <= profundidade_caixa)):
    print('cabe')
else:
    print('nao cabe')
