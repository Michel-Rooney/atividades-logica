# Escreva um programa em Python que receba uma string do usuário e mostre de trás pra frente

texto = str(input('Digite uma frase: '))
print(f'O texto de trás pra frente é: {texto[::-1]}')

for i in range(len(texto) -1, 0, -1):
    txt = ' '.join(texto[i])

print(txt)