# Faça um algoritmo que leia um número e escreva se está entre 500 e 1000 ou entre 1001 e 2000, ou ainda entre 3000 e 4000

num = int(input('Digite um número: '))

if num >= 500 and num <= 1000:
    print('O número está entre 500 e 1000')
elif num >= 1001 and num <= 2000:
    print('O número está entre 1001 e 2000')
elif num >= 3000 and num <= 4000:
    print('O número está entre 3000 e 4000')
else:
    print('O número não pertence a nenhum grupo')
   