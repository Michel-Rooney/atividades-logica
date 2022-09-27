# Construa um algoritmo que leia e imprima a altura de 500 pessoas um a uma. No final escrever a média das alturas lidas

cont = 1
soma = 0

while cont <= 5:
    altura = float(input(f'Digite a altura dá {cont}ª pessoa: '))
    if altura < 0 or altura > 3:
        print('altura inválida')
        continue
    soma += altura
    cont += 1

media = soma / cont
print(f'A média entre os valores é {media:.2f}')
