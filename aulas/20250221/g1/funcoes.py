# Objetivo: Função para calcular a quantidade de vogais em um texto.
# Parâmetro: str (texto)
# Retorno: int (quantidade de vogais)
def quantidade_vogais(texto):
    vogais = 'aeiouAEIOU'
    qtd = 0
    for i in range(len(texto)):
        if texto[i] in vogais:
            qtd += 1
    return qtd


# Objetivo: Função para calcular a quantidade de letras maiúsculas.
# Parâmetro: str (texto)
# Retorno: int (quantidade de letras maiúsculas)
def quantidade_letras_maiusculas(texto):
    qtd = 0
    for i in range(len(texto)):
        if texto[i].isupper() == True:
            qtd += 1
    return qtd


# Objetivo: Função para calcular a quantidade de dígitos numéricos.
# Parâmetro: str (texto)
# Retorno: int (quantidade de dígitos numéricos
def quantidade_digitos_numericos(texto):
    qtd = 0
    for i in range(len(texto)):
        if texto[i].isdigit() == True:
            qtd += 1
    return qtd


# Objetivo: Exibir os símbolos distintos de um texto.
# Parâmetro: str (texto)
# Retorno: 
def simbolos_distintos(texto):
    memoria = []
    for i in range(len(texto)):
        if texto[i] not in memoria:
            memoria.append(texto[i])
    print(memoria)
        









