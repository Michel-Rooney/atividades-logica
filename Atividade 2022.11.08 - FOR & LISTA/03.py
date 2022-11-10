lista_par = []
lista_impar = []
n = int(input('Digite a quantidade de repetições: '))
for i in range(1, n+1):
    idade = int(input('Digite a sua idade: '))
    if idade % 2 == 0:
        lista_par.append(idade)
    else:
        lista_impar.append(idade)
print(lista_par)
print(lista_impar)