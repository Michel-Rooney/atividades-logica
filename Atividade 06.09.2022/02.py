# Faça um algoritmo que leia um número maior que 4 e depois de lido dizer se este número é par ou impar. Se o número lido não for
# maior que 4 não executar o algoritmo e mandar um aviso dizendo que o algoritmo só pode funcionar com um número maior que 4

num = int(input('Digite um número: '))

if num < 4:
    print('O programa só funciona com números maior que 4')
else:
    print(f'{num} é PAR' if num % 2 == 0 else f'{num} é IMPAR')


