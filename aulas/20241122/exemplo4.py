lista = [10,20,30,20,40,20,50,20]

qtd_20 = lista.count(20)

for i in range(qtd_20):
    lista.remove(20)

print(lista)
