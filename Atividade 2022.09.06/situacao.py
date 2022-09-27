n1 = float(input('Dgite a 1ª nota: '))
n2 = float(input('Dgite a 2ª nota: '))
n3 = float(input('Dgite a 3ª nota: '))
n4 = float(input('Dgite a 4ª nota: '))

media = (n1 + n2 + n3 + n4) / 4
print(f'A media final do aluno eh: {media:.2f}')

if media < 6:
    recuperacao = float(input('Diigte a nota de recuperação: '))
    if recuperacao >= 6:
        print('APROVADO na Recuperação')
    else:
        print('REPROVADO')

else:
    print('Aprovado por Media')
