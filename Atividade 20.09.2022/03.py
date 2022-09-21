# Faça um algoritmo que calcule para uma turma de 45 alunos o seguinte
# A idade média dos alunos da sala
# A altura média dos alunos da sala


n = 0
sum_idades = 0
sum_alturas = 0
while n < 5:
    idade = int(input('Digite sua idade: '))
    altura = int(input('digite sua altura em centimetros: '))

    sum_idades += idade
    sum_alturas += altura
    n += 1
else:
    media_idade = sum_idades / 5
    media_alturas = sum_alturas / 5

    print(f'A media das alturas dos 45 alunos é {media_idade:.2f}')
    print(f'A media das alturas dos 45 alunos é {media_alturas:.2f}')
