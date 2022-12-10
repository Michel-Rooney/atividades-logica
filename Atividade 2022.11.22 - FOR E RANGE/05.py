# Escreva um programa em Python para encontrar o fatorial de qualquer número

n = int(input('Digite um número para encontrar seu fatorial: '))
fatorial = 1
for i in range(n, 0, -1):
    print(i)
    fatorial *= i

print(f'O fatorial de {n} é {fatorial}')