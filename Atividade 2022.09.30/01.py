cont = 1
total_ingresso = 0

while cont <= 100:
    n = int(input(f'Pessoa {cont} digite sua idade: '))
    if n >= 0 and n < 3:
        print('Menores de 3 anos não preicsam pagar')
    elif n >= 3 and n < 12:
        print('Entre 3 e 12 anos paga R$10,00')
        total_ingresso += 10
    elif n >= 13 and n <= 120:
        print('Pessoas acima de 12 anos pagam R$15,00') 
        total_ingresso +=  15
    else:
        print('Digite uma idade válida')
        continue
    cont += 1


print(f'A soma de todos os ingressos é {total_ingresso}')