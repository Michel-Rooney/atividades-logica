# Faça um algoritmo que para N números inteiros, divida cada número por um número inteiro ímpar lido também. Em seguida, escreva apenas a parte inteira do resultado e o resto da divisão.

cont = 1

while cont <= 10:
    if cont == 1:
        impar = int(input('Digite um núemro impar: '))
        if impar % 2 == 0:
            print('Digite um número impar valido')
