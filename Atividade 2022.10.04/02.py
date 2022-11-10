# Um fazendeiro quer fazer um programa para saber quantos quilos de leite ele tira de suas 100 vacas em uma semana. Faça um algoritmo que calcule a quantidade de leite de cada vaca por dia até chegar a uma semana e a média do leite todo escrevendo a informação.


cont_dia, cont_vaca, soma_leite, soma_leite_dia, media_dia, media_semana = 1, 1, 0, 0, 0, 0

while cont_dia <= 2:
    print(f'\n{cont_dia}º Dia')
    while cont_vaca <= 3:
        leite = float(input(f'quantida de leite da vaca {cont_vaca}: '))
        soma_leite += leite
        cont_vaca += 1
    cont_vaca = 1
    media_dia = soma_leite / 3
    soma_leite_dia += media_dia
    cont_dia += 1

media_semana = soma_leite_dia / 2
print(media_semana)
