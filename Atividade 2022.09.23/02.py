# Calcular a média aritmética de N números inteiros lidos

n = int(input('Digite a quantidade de valores que queres fazer a média: '))
soma = 0
cont = 1

while cont <= n:
    num = int(input(f'Digite o {cont}ª número: '))
    soma += num
    cont += 1

media = soma / n
print(f'A média dos valores é {media}')
