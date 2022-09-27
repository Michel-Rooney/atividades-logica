# Faça um algoritmo que calcule para uma turma de 45 alunos o seguinte
#   - A idade média dos alunos com menos de 1.70m de altura
#   - A altura média dos alunos com mais de 20 anos


cont = 1
cont_altura = 0
cont_altura_idade = 0
soma_altura = 0
soma_altura_idade = 0

while cont <= 45:
    altura = float(input('Digite sua altura: '))
    if altura < 0 or altura > 3:
        print('Altura inválida')
        continue
    if altura < 1.70:
        soma_altura += altura
        cont_altura += 1

    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 120:
        print('Idade inválida')
        continue
    if idade > 20:
        soma_altura_idade += altura
        cont_altura_idade += 1

    cont += 1

media_altura = soma_altura / cont_altura
media_altura_idade = soma_altura_idade / cont_altura_idade

print(f'A média dos alunos com menos de 1.70 é: {media_altura:.2f}')
print(f'A altura média dos alunos com mais de 20 anos é: {media_altura_idade:.2f}')
