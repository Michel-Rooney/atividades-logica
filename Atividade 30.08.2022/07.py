# Um revendora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. escrever um algorotimo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor

salario = float(input('Digite seu salario: '))
comissao = float(input('Digite a comissão por carros: '))
vendas = float(input('Digite o valor das vendas no mês: '))
carros = int(input('O número de carros que voce vendeu: '))

salario_final = salario + (vendas*0.05) + (comissao * carros)
print(f'O salario final é: {salario_final:.2f}')
