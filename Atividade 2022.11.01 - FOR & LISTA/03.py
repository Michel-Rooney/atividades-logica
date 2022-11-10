# Criei uma lista e armazene somente numeros impares na lista. Deopois exiba a lista

impares = []
for _ in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 1:
        impares.append(num)

print(impares)