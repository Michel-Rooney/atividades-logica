# Sabendo que alguns tabalhadores terão um reajuste de x% sobre seus salários, faça um algoritmo que: Leia a quantidade de trabalhadores e, para cada um, leia seu nome, o valor do salário e o percentural de aumento e escreva o nome o salário antigo e novo salário de cada trabalhador

quant_trabalhadores = int(input('Digite a quantidade de trabalhores: '))
cont = 1
while cont <= quant_trabalhadores:
    nome = str(input('Seu Nome: '))
    salario = float(input('Seu salário: '))
    percentual = float(input('Digite o percentual: '))
    novo_salario = ((salario * percentual) / 100) + salario

    print(f'Nome: {nome}\nSalário Antigo: {salario}\nSalário Novo: {novo_salario}\n')
    cont += 1