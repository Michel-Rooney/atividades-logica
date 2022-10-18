# Construa um algoritmo que pegue o nome e a idade de 100 pessoas, idade validas e diga qual a maior e menor idade


cont = 1
maior = 0
menor = 120

while cont <= 5:
    nome = str(input('Digite seu nome: '))
    idade = int(input(f'Digite a idade de {nome}: '))

    if idade < 0 and idade > 120:
        print('Idade inválida')
        continue
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
    cont += 1

print(f'Maior idade {maior}')
print(f'Menor idade {menor}')
