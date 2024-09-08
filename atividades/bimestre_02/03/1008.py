numero  = int(input('Número: '))
horas = int(input('Horas Trabalhadas: '))
valor_hora = float(input('Valor da hora trabalhada: '))

salario = horas * valor_hora

print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')