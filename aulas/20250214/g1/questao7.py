"""
7. Escreva um programa para ler uma frase e exibir
   quantas palavras ela possui.
"""

frase = input('Digite uma frase: ')

# solução "no braço"
qtd_palavras = 0
qtd_espacos = 0

for i in range(len(frase)):
    if frase[i] == ' ':
        qtd_espacos += 1

qtd_palavras = qtd_espacos + 1

print(qtd_espacos)
print(qtd_palavras)


# solução com "count"
qtd_palavras = frase.count(' ') + 1
print(qtd_palavras)

# solução com "split"
qtd_palavras = len(frase.split())
print(qtd_palavras)
