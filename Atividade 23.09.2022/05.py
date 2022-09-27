# Faça um algoritmo que leia 50 números reais e escreva o número maior e o menor deles

cont = 1
maior = 0
menor = 999999999999999999999999999

while cont <= 50:
    num = float(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    cont += 1

print(f'O valores são:\nMaior: {maior}\nMenor: {menor}')
