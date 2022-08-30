# Um revendora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. escrever um algorotimo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor

salario_fixo = 1200.00
comissao_fixa = 20
num_carros = int(input('Digite a quantidade de carros vendidos: '))
comissao_carros = 20 * num_carros
valor_total_vendas = (5/100)*comissao_carros
valor_total = salario_fixo + comissao_carros + valor_total_vendas

print(f'Ele irar receber {valor_total}')

# valor_total_vendas = 
# valor_por_carro_vendido = 