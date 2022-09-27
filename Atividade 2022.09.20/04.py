# Faça um algoritmo que imprima a multiplicação do número 7 po 1, por 2, por 3 ..., por 100

n = 1
v = int(input('Digite um valor: '))
while n < 101:
    print(f'{v} x {n} = {v * n}')
    n += 1


# v = int(input('Digite um valor: '))
# for i in range(1, 101):
#     print(f'{v} x {i} = {v * i}')
    