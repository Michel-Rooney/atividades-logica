# Faça um algoritmo para ler dois números reais e testar se formam um retângulo. Se formar, calcular seu perímetro e sua área. Depois de calculado o perímetro e a área, ler um outro número real e se puder, calcular o volume deste paralelepipedo. No final escrever os três lados, o perímetro e a área do retângulo e o volume do paralelepipedo.
# Observação -> Deixar o algoritmo perfeito dando resposta no escreva (write) para qualquer número(s) lido(s)
# cálculo do perimetro -> (num1 + num2) * 2
# cálculo da área -> num1 * num2
# cálculo do volume -> num1 * num2 * num3
# Não esqueçam qe um quadrado também é um retângulo

base = abs(float(input('Digite a base do retângulo: ')))
altura = abs(float(input('Digite a altura do retângulo: ')))
largura = abs(float(input('Digite o volume desse retangulo: ')))

if base == altura:
    print('Não é possivel formar um retangulo')
else:
    perimetro = (base + altura) * 2
    area = base * altura
    volume = base * altura * largura

    print('foda')




