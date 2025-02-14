idade_st = input('Digite sua idade: ')

while (idade_st.isdigit() == False):
    print('errada')
    idade_st = input('Digite sua idade: ')

idade_int = int(idade_st)
dobro_idade = idade_int * 2
print(f'Dobro de {idade_int} = {dobro_idade}')
