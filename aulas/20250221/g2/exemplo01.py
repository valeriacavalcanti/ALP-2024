# Objetivo: somar dois valores inteiros, desde que sejam não negativos
# Parâmetros: int int
# Retorno: int
def somar(n1, n2):
    soma = 0
    if (n1 >= 0):
        soma += n1
    if (n2 >= 0):
        soma += n2
    return soma


# PROGRAMA PRINCIPAL
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

soma = somar(num1, num2)

print(f'{num1} + {num2} = {soma}')

# testar
print(somar(10,20))     # 30
print(somar(10,-10))    # 10
print(somar(10, 0))     # 10
print(somar(20,-10))    # 20
