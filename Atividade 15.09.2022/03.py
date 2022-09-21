def leia_int(texto):
    while True:
        try:
            num = int(input(texto))
            if num < 0 or num > 116:
                print('Idade inválida')
                continue
        except (ValueError, TypeError):
            print('Digite um opção válida')
        except KeyboardInterrupt:
            print('Você ousou aperta CTRL + C')
        else:
            return num


idade = leia_int('\nDigite sua idade: ')

if (idade >= 0) and (idade < 2):
    print('Você é um bebê')
elif (idade >= 2) and (idade < 4):
    print('Você é uma criança')
elif (idade >= 4) and (idade < 13):
    print('Você é um garoto(a)')
elif (idade >= 13) and (idade < 20):
    print('Você é um adolescente')
elif (idade >= 20) and (idade < 65):
    print('Você é um adulto')
elif idade >= 65:
    print('Idoso')
