# função para somar dois valores
def soma_simples(n1, n2):
    soma = n1 + n2
    return soma


# PROGRAMA PRINCIPAL
num1 = int(input('Número: '))
num2 = int(input('Número: '))

soma = soma_simples(num1, num2)

print(soma)
