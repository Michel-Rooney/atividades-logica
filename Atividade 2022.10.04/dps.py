# pegar a media de 4 notas de um aluno de cada turma
# nome da turma, dps aluno, dps nota


cont_turna = 1
cont_aluno = 1
cont_nota = 1

soma_nota = 0
soma_turma = 0

media_aluno = 0
media_turma = 0

while cont_turna <= 2:
    nome_turma = str(input('Digite o nome da turma: '))
    print(f'\nTurma {nome_turma}')
    while cont_aluno <= 2:
        nome = str(input(f'\nDigite o nome do {cont_aluno}ª aluno: '))
        print(f'\nNotas do {nome}')
        while cont_nota <= 4:
            nota = float(input(f'{cont_nota} Nota: '))
            soma_nota += nota
            cont_nota += 1
        cont_nota = 1
        media_aluno = soma_nota / 4
        print(f'A média do {nome} é {media_aluno}')
        soma_turma += media_aluno
        cont_aluno += 1
        soma_nota = 0
    media_turma = soma_turma / 2
    cont_aluno = 1
    print(f'\nA média da turma {nome_turma} é {media_turma}\n')
    media_turma = 0
    soma_turma = 0
    cont_turna += 1

