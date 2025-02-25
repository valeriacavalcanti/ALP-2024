import random

# função para somar dois valores
def soma_simples(n1, n2):
    soma = (n1 + n2) * 2
    return soma

# função para exibir informações sobre o software
def informacoes():
    print('--------------------------------')
    print('Instituição: IFPB')
    print('Curso: Integrado em Informática')
    print('Ano: 1')
    print('Disciplina: ALP')
    print('--------------------------------')
    print()

# exibir "IFPB" de acordo com quantidade estabelecida.
def print_ifpb(quantidade):
    for i in range(quantidade):
        print('IFPB')

    print('---')

# Gerar um valor aleatório entre 0 e 100
def valor_aleatorio():
    valor = random.randint(0, 100)
    return valor


# PROGRAMA PRINCIPAL
informacoes()

print_ifpb(4)

v1 = valor_aleatorio()
v2 = valor_aleatorio()

soma = soma_simples(v1, v2)

print(v1,v2,soma)
