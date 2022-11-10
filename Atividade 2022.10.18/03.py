# Contrua um algoritno que receva 1000 valores e informe a quantidade ímpares e a quantidade de pares, critique valores dentro do intervalo de [0 .. 80]

cont = 1
impar = 0
par = 0


while cont <= 5:
    num = int(input('Digite um valor: '))
    if num < 0 and num > 80:
        print('O valor digitado tem que ser entre 0 e 80')
    else:
        if num % 2 == 0:
            par += 1
        if num % 2 == 1:
            impar += 1

        cont += 1

print(f'Pares: {par}')
print(f'Impares: {impar}')





