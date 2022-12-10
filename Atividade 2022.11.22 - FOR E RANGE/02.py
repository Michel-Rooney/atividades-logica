# Crie um programa em Python para contar a quantidade de números pares e ímpares de uma série de números

list_num = []

while True:
    num = int(input('Digite um número: '))
    list_num.append(num)
    stop = int(input('[1] Continuar\n[2] Parar\n: '))
    if stop == 2: break


pares, impares = 0, 0
for i in list_num:
    if i % 2 == 0: pares += 1
    else: impares += 1

print(f'Números digitados: {list_num}')
print(f'Quantidade números pares: {pares}')
print(f'Quantidade números impares: {impares}')
