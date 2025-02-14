
while True:
    idade_st = input("Idade: ")
    if (idade_st.isdigit() == True):
        break
    print('tá errado')


idade_int = int(idade_st)
dobro = idade_int * 2
print(idade_int, dobro)
