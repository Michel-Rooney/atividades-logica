# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1

num = int(input('Digite um número: '))
mult = 0
for i in range(2, num):
    if num % i == 0:
        mult += 1

if mult == 0:
    print('É primo')
else:
    print('Não é primo')
