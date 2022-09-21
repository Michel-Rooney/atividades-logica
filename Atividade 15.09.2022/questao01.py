alien_color = str(input("Digite a cor do alien: "))

if (alien_color == "GREEN") or (alien_color == "YELLOW") or (alien_color == "RED"):
    if (alien_color == "GREEN"):
        print("O jogador ganhor +5 pontos")
    else:
        print("A cor é valida, porem o jogador nao ganhou nada.")
else:
    print("A cor do alien é inválida")
