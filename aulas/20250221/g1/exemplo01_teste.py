# função para somar dois valores
def soma_simples(n1, n2):
    soma = (n1 + n2) * 2
    return soma


# PROGRAMA PRINCIPAL
soma1 = soma_simples(10, 20)
soma2 = soma_simples(10, -10)
soma3 = soma_simples(-10, -10)
soma4 = soma_simples(10, 0)

print(soma1)    # 60
print(soma2)    # 0
print(soma3)    # -40
print(soma4)    # 20
