# Faça um algoritmo em py que imforme o nome, a agencia, a conta de uma pessoa. Peça que ela informe a senha 3 vezes. Se em todas as senhas forem iguais, diga "Usuário Válido", caso contrário informe que o usuário é inválido, tudo isso usando while

nome = str(input('Digite seu nome: '))
agencia = str(input('Digite sua agencia: '))
conta = int(input('Digite o numero da conta: '))

cont = 1
while cont <= 3:
    senha = str(input(f'Digite sua senha {cont}: '))

    if cont == 1:
        senha1 = senha
    elif cont == 2:
        senha2 = senha
    elif cont == 3:
        senha3 = senha
    cont += 1

if senha1 == senha2 == senha3:
    print('Usuário válido')
else:
    print('Usuário inválido')
    