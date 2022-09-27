# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias

idade = int(input('Digite sua idade: '))
print(f'Sua idade em meses é: {idade * 12}')
print(f'Sua idade em dias é: {idade * 365}')
