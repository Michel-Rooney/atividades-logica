# Faça um algoritmo que calcule a soma do peso de N pessoas maior que 60 quilos e menor que 100 quilos.

cont = 1
soma = 0
while cont <= 10:
    peso = float(input(f'Peso {cont} pessoa: '))
    if (peso <= 0) or (peso > 220):
        print('Peso inválido. Digite novamente\n')
        continue
    if (peso >= 60) and peso (peso <= 100):
        soma += peso

    cont += 1

print(f'A  soma dos pesos entre 60 e 100 kg é {soma}')
