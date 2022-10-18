# Contrua um algoritmo que receba a nota de 45 alunos, diga a média e a maior nota

maior = 0
soma = 0
cont = 1
while cont <= 45:
    nota = float(input('Digite sua nota: '))
    soma += nota
    if nota > maior:
        maior = nota
    cont += 1
media = soma / 45

print(f'Média: {media}')
print(f'Maior: {maior}')

