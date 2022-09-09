# Faça um algoritmo para ler dois números e se a soma dos dois números lidos for par trocar o conteúdo de uma variável pela outra.

n1 = int(input('Digite 1ª número: '))
n2 = int(input('Digite 2ª número: '))

if (n1 + n2) % 2 == 0:
    n1 += n2

print(n1, n2)