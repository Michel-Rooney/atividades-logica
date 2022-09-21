# Elabore um algoritmo que faça a média aritimética de dez númereos interiros lidos escrevendo os números, sua média e se a média é menor ou igual a DEZ, se é maior que DEZ e menor ou igual a CINQUENTA ou ainda se a média é maior que CIQUENTA

notas = [] # Diz que a var losta vai ser uma lista
for i in range (1, 11):
    n = int(input(f'Digite o {i}º núnero: '))
    notas.append(n) # O append serve para adicionar um novo valor a lista, que o mesmo é n

media = sum(notas) / len(notas) # um sum vai somar todos os valores da lista (n + n + n) / len vai pegar o tamanho da lista (n, n, n) = 3

print(f'A média é {media:.2f}')
if media <= 10:
    print('A média é menor ou igual a 10')
elif media > 10 and media <= 50:
    print('A media é maior que dez e menor ou igual a ciquenta')
elif media > 50:
    print('A media é maior que ciquenta')
