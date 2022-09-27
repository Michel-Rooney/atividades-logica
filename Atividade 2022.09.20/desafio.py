# DESAFIO - Uma   escola  precisa  ler  e  imprimir  a  médias  de  seus 12 alunos nas 20 ( vinte ) notas  tiradas  por  cada  um  no  ano letivo. Faça um algoritmo que escreva o nome e a média de cada aluno e a média geral de toda a turma.

x = 1
y = 1
sum_notas = 0
sum_notas_aluno = 0
while x < 13:
    while y < 21:
        n = int(input(f'Digite a {y}ª nota do {x}ª aluno: '))
        sum_notas_aluno += n
        media_aluno = sum_notas_aluno / 20
        y += 1

    print(f'A média do {x}º aluno é {media_aluno}')
    sum_notas += media_aluno
    sum_notas_aluno = 0
    y = 1
    x += 1
else:
    media = sum_notas / 12
    print(f'A média dos alunos dá escola é {media}')
