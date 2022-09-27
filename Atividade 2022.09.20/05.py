# Calcular a média aritmética de N números lidos somando somente os ímpares

n = int(input('Digite a quantidade: '))
x = 1
cont = 0
sum_num = 0
while x < n + 1:
    v = int(input(f'Digite o {x}ª valor: '))
    if v % 2 == 1:
        sum_num += v
        cont += 1
    x += 1
print(sum_num / cont)


