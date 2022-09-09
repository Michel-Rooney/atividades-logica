# Elabore um algoritmo que faça a média aritimética de dez númereos interiros lidos escrevendo os números, sua média e se a média é menor ou igual a DEZ, se é maior que DEZ e menor ou igual a CINQUENTA ou ainda se a média é maior que CIQUENTA

notas = []
for i in range (1, 11):
    n = int(input(f'Digite o {i}º núnero: '))
    notas.append(n)

media = sum(notas) / len(notas)

print(f'A média é {media:.2f}')
if media <= 10:
    print('A média é menor ou igual a 10')
elif media > 10 and media <= 50:
    print('A media é maior que dez e menor ou igual a ciquenta')
elif media > 50:
    print('A media é maior que ciquenta')
