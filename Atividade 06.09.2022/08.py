# Faça um algoritmo que leia um nome e um endereço, bairro, cidade, escreva seu nome, seu endereço, seu bairro, com detalhe se a cidade for SOBRAL escrever depois de escrever a cidade PRINCESINHA DO NORTE se a cidade for CAMOCIM escrever depois de escrever a a cidade CIDADE DAS PRAIAS LINDAS qualquer outra cidade escrever depois de escrever a cidade SUA CIDADE EH BELA TAMBEM

endereco = str(input('Digite seu endereço: ')).capitalize()
bairro = str(input('Digte o nome do seu bairro: ')).capitalize()
cidade = str(input('Digite sua cidade: ')).capitalize()

print(f'Endereço: {endereco}\nBairro: {bairro}\nCidade: {cidade}')
if cidade == 'Sobral':
    print('Pricesinha do norte')
elif cidade == 'Camocim':
    print('Cidade das praias lindas')
else:
    print('Sua cidade é bela também')
