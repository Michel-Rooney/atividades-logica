# Escreva um algoritmo para ler o salário mensal atual de um funcionárioe o percentual de reajuste.
# Calcular e escrever o valor do novo salário

salario = float(input('Digite seu salário: '))
reajuste = float(input('Digite o valor de reajuste: '))

novo_salario = salario + ((reajuste/100)*salario)
print(f'''
Antigo salário: {salario}
Reajuste: {reajuste}%
Novo salário: {novo_salario}
''')
