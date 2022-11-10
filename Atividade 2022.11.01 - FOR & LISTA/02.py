# Crie uma lista de idades e exiba os valores da lista apenas os pares

idades = []
for i in range(0, 10):
    idade = int(input('Digite sua idade: '))
    idades.append(idade)

# while True:
#     idade = int(input('Digite sua idade: '))
#     idades.append(idade)
#     stop = int(input('[1] Digita mais uma idade\n[2] Parar\n: '))
#     if stop == 2:
#         break

for i in idades:
    if i % 2 == 0:
        print(i)
