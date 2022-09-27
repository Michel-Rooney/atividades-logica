# Para se obter a inplicação da taxa atual da inflação, teriamos que comprar o preço pago hoje por um produto pelo preço dele há um tepo atrás
# ValorInflação = (preçoatual - preçoantigo)/preçoantigo * 100
# Faça um algoritmo que sabendo os dois preços pagos por um produto, imprima o nome, o preço atual, o preço antigo, a diferença alhebrica e a taxa de inflação

preco_antigo = float(input('Digite o preço antigo do produto: '))
preco_atual = float(input('Digite o preço atual do produto: '))

diferenca_algebrica = preco_antigo - preco_atual
valor_inflacao = ((preco_atual - preco_antigo) / preco_antigo) * 100

print(f'Preços:\nAntigo: {preco_antigo}\nNovo: {preco_atual}\nInflação: {valor_inflacao}\nInflação algebrica: {diferenca_algebrica}')
