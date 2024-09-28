valor_compra = float(input('Valor da compra: '))

if (valor_compra <= 100):
    print('2 parcelas')
elif (valor_compra <= 500):
    print('4 parcelas')
elif (valor_compra <= 1000):
    print('6 parcelas')
else:
    print('10 parcelas')