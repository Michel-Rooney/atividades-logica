# Faça um algoritmo que leia 3 nomes e escreva se um, ou dois, ou ainda os três nomes são iguais(s) a João ou diferente

n1 = str(input('Nome1: '))
n2 = str(input('Nome2: '))
n3 = str(input('Nome3: '))

nomes_iguais = 0

if n1 == 'João':
    nomes_iguais += 1
elif n2 == 'João':
    nomes_iguais += 1
elif n3 == 'João':
    nomes_iguais += 1

print(f'Tem {nomes_iguais} com nomes igual a João')
