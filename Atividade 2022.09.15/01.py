def leia_int(texto):
    while True:
        try:
            cor = int(input(texto))
            if cor < 1 or cor > 3:
                print('Opção inválida')
                continue
        except (ValueError, TypeError):
            print('Digite um opção válida')
        except KeyboardInterrupt:
            print('Você ousou aperta CTRL + C')
        else:
            return cor


cor_alien = leia_int('\nEscolha uma das opções abaixo:\n[1] Green\n[2] Red\n[3] Yellow\n: ')
pontos_jogador = 0

if cor_alien == 1:
    print('Saudações terraquios')
    pontos_jogador += 5
else:
    print('Você errou a cor')
