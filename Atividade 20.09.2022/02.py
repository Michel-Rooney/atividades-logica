# Construa um algoritmo que leia e imprima a idade de 100 pessoas um a uma. No final escrever a média das idades lidas

n = 0
idades = 0
while n < 100:
    idade = int(input('Digite sua idade: '))
    idades += idade
    n += 1
else:
    media = idades / 100
    print(f'A media das idades é {media}')
