# Calcular a média aritmética de N números lidos somando somente os ímpares

n = 0
sum_num = 0
while n < 100:
    if n % 2 == 1:
        sum_num += n
    n += 1
print(sum_num / 100)
