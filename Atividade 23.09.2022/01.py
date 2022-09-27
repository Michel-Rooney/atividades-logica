# Faça um algoritmo que leia e imprima o peso de mil pessoas uma a uma

cont = 1
while cont < 1001:
    peso = float(input('Digite seu peso: '))
    print(f'O peso dá {cont}ª pessoa é {peso}kg')
    cont += 1
