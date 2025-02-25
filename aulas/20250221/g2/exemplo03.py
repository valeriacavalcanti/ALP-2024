# Objetivo: Exibir todos os símbolos numéricos.
# Parâmetro: 
# Retorno: 
def exibir_simbolos_numericos():
    for i in range(10):
        print(i)


# Objetivo: Exibir todos os símbolos do alfabeto maiúsculo.
# Parâmetro: 
# Retorno: 
def exibir_simbolos_maiusculos():
    cod_A = ord('A')
    cod_Z = ord('Z')
    for i in range(cod_A, cod_Z + 1):
        print(chr(i))


# PROGRAMA PRINCIPAL

#exibir_simbolos_numericos()
exibir_simbolos_maiusculos()
