while True:
    idade_st = input('Digite sua idade: ')
    
    if idade_st.isdigit() == True:
        break
    
    print('errada')

idade_int = int(idade_st)
dobro_idade = idade_int * 2
print(f'Dobro de {idade_int} = {dobro_idade}')
