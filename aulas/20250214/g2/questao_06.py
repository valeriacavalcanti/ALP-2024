"""
    6. Escreva um programa para ler uma frase e exibir
    quantas vezes aparece o símbolo“A” (A – maiúsculo).
"""

# ler a frase
frase = input('Digite uma frase: ')

# contador da letra A
qtd_A = 0

# percorrer a frase
for i in range(len(frase)):
    # verificar se o símbolo é a letra A
    if (frase[i] == 'A'):
        qtd_A += 1

print(qtd_A)
