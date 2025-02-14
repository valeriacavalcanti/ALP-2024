st = "bolo chocolate bolo ingles bolo baeta bolo laranja bolo!"
tamanho = len(st)

#print(st.count('bolo'))

start = 0
print(st.find('bolo', start, tamanho))

start = 1
print(st.find('bolo', start, tamanho))
