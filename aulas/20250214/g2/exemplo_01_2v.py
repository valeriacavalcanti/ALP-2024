idade_st = input("Idade: ")

while idade_st.isdigit() == False:
    print('tá errado')
    idade_st = input("Idade: ")


idade_int = int(idade_st)
dobro = idade_int * 2
print(idade_int, dobro)
