"""
    8. Escreva um programa para ler uma frase e exibir:
        a. Quantidade de letras maiúsculas;
        b. Quantidade de letras minúsculas;
        c. Quantidade de símbolos numéricos.
"""

frase = input('Frase: ')
qtd_maiuscula = 0
qtd_minuscula = 0
qtd_simbolo_numerico = 0

for i in range(len(frase)):
    
    if (frase[i] >= '0') and (frase[i] <= '9'):
        qtd_simbolo_numerico += 1
    else:
        if (frase[i] >= 'A') and (frase[i] <= 'Z'):
            qtd_maiuscula += 1
        else:
            if (frase[i] >= 'a') and (frase[i] <= 'z'):
                qtd_minuscula += 1

print(f"Letras maiúsculas: {qtd_maiuscula}")
print(f"Letras minúsculas: {qtd_minuscula}")
print(f"Símbolos numéricos: {qtd_simbolo_numerico}")
