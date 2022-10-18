# Faça um algoritmo que dada a quantidade de pessoas de sua familia, calcule a mpedia de idade, no final, mostre o nome, a idade de cada pessoa e por ultimo a média de idade dos mesmo

quantida_familia = int(input('Quantas pessoas tem na sua fámilia: '))
cont = 1
media = 0
soma = 0

while cont <= quantida_familia:
    nome = str(input('Digite seu nome: '))
    idade = int(input(f'Digite a idade da {nome}: '))
    print(f'{nome} tem {idade} anos')
    soma += idade
    cont += 1
media = soma / quantida_familia
print(f'A media de idades é {media}')
