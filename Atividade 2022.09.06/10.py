# Faça um algortimo para ler dois números e se a soma dos dois números lidos for par trocar o conteúdo de uma variável pela outra

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2

print(f'Você digitou os números n1:{n1} n2:{n2}')
if soma % 2 == 0:
    print('A soma dos número é par')
    n1 = soma - n1
    n2 = soma - n2
else:
    print('A soma é impar')
print(f'Agora os números são n1:{n1} n2:{n2}')

