# Utilizando a estrutura de repetição for, faça um programa em Linguagem Python que receba 10 números e conte quantos deles estão no intervalo [10, 20] e quantos deles estão fora do intervalo, escrevendo estas informações.

lista_num = []
intervalo = list(range(10, 21))
dentro, fora = 0, 0
for i in range(1, 11):
    num = int(input(f'Digite o {i}º número: '))
    lista_num.append(num)
    
    if num in intervalo: dentro += 1
    else: fora += 1

print(f'Num digitados: {lista_num}')
print(f'Quantidade de números dentro: {dentro}')
print(f'Quantidade de números fora: {fora}')


