# Objetivo: Calcular a quantidade de símbolos numéricos em um texto. 
# Parâmetro: str
# Retorno: int
def contar_simbolos_numericos(texto):
    qtd = 0
    for i in range(len(texto)):
        if texto[i].isdigit() == True:
            qtd += 1
    return qtd


# Objetivo: Calcular a quantidade vogais no texto. 
# Parâmetro: str
# Retorno: int
def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    qtd = 0
    for i in range(len(texto)):
        if texto[i] in vogais:
            qtd += 1
    return qtd


# Objetivo: Calcular a quantidade de palavras em um texto. 
# Parâmetro: str
# Retorno: int
def contar_palavras(texto):
    lista = texto.split()
    tamanho = len(lista)
    return tamanho

























    
