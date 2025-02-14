"""
    Escreva um programa para ler uma frase e exibir:
    a. Quantidade de letras maiúsculas (isupper);
    b. Quantidade de letras minúsculas (islower);
    c. Quantidade de símbolos numéricos (isdigit).
"""

frase = input('Frase: ')

qtd_maiuscula = 0
qtd_minuscula = 0
qtd_simbolo_numerico = 0

"""
for i in range(len(frase)):
    if ((frase[i] >= 'A') and (frase[i] <= 'Z')):
        qtd_maiuscula += 1
    elif ((frase[i] >= 'a') and (frase[i] <= 'z')):
        qtd_minuscula += 1
    elif ((frase[i] >= '0') and (frase[i] <= '9')):
        qtd_simbolo_numerico += 1
"""

for i in range(len(frase)):
    if (frase[i].isupper() == True):
        qtd_maiuscula += 1
    elif (frase[i].islower() == True):
        qtd_minuscula += 1
    elif ((frase[i].isdigit() == True):
        qtd_simbolo_numerico += 1

print(qtd_maiuscula, qtd_minuscula, qtd_simbolo_numerico)



