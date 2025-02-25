# Objetivo: Exibir um númeiro inteiro por extenso.
# Parâmetro: int
# Retorno:
def exibir_extenso(num):
    numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

    print(numeros[num])


# PROGRAMA PRINCIPAL

exibir_extenso(0)

for i in range(10):
    exibir_extenso(i)
