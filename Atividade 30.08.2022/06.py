# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicação ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,, calcular e escrever o custo final ao consumidor

preco_fabrica = float(input('Digite o valor do carro: '))
preco_final = preco_fabrica + ((28/100 + 45/100)*preco_fabrica)

print(f'O preço final do carro é {preco_final}')